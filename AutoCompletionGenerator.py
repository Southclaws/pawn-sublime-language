import sys
import os
import glob
import string


# Regular expressions for defines, natives and publics.
# I decided against using regex eventually for a few reasons.
# re_define = r"\#define\s*(.*)[ 	]"
# re_native = r"native\s*([A-Za-z0-9:]*)([A-Za-z0-9_]*)\((.*)\);"
# re_public = r"forward\s*([A-Za-z0-9:]*)([A-Za-z0-9_]*)\((.*)\);"


# quick and dirty debug prints that can be toggled

debug = False


def db(*args):
	if not debug:
		return

	for i in args:
		print(i, end=" ")

	print("")


def gen_func(funcname, params):
	"""generates a sublime-completions line based on a function"""

	out = '\t\t{"trigger": "%s", "contents": "%s(' % (funcname, funcname)

	for i, param in enumerate(params):
		out += '${%d:%s}' % (i + 1, param.replace('\\', '\\\\').replace('"', '\\\"'))

		if(i != len(params) - 1):
			out += ', '

	out += ')"},\n'

	return out


def gen_const(string):
	"""generates a sublime-completions line based on a single string"""
	args = string
	if "%" in string:
		i = 0
		for x in range(-1, 9):
			if string.find("%%%d" % (x)) != -1:
				i += 1
				args = args.replace("%%%d" % (x), "${%d:%d}" % (i, x))
		out = '\t\t{"trigger": "%s", "contents": "%s' % (string, args)
		out += '"},\n'
	else:
		out = '\t\t"%s",\n' % string
	return out


def is_char_valid_symbol_char(character):
	return (
		character in string.ascii_lowercase +
		string.ascii_uppercase + string.digits + '_'
	)


def scan_contents(contents):
	"""
	scans through a string character by character extracting defines and
	functions
	"""

	output_contents = """
{
	"scope": "source.pawn - variable.other.pawn",
	"completions":
	[
"""

	skip_until_newline = False
	skip_until_whitespace_start = False
	skip_until_whitespace_end = False
	skip_until_invalid_symbol_char = False
	skip_until_valid_symbol_char = False
	in_comment_block = False
	in_directive = False
	in_directive_define = False
	pos_directive_define = -1
	in_function = False
	in_function_declare = False
	in_function_params = False
	pos_function_name = -1
	pos_function_param = -1
	data_function_name = ""
	data_function_params = []
	# count_function_params = 0
	in_function_param_subscript = False
	in_function_param = False
	no_function_params = False
	# in_enumerator = False
	# in_enumerator_block = False
	# pos_enumerator_item = -1

	for i, c in enumerate(contents):

		db(i, c)

		if skip_until_newline:
			if c == '\n':
				skip_until_newline = False
				db("skipped until newline found at ", i)
				continue

			else:
				continue

		if skip_until_whitespace_start:
			if c.isspace():
				skip_until_whitespace_start = False
				db("skipped until whitespace found at ", i)

			else:
				continue

		if skip_until_whitespace_end:
			if not c.isspace():
				skip_until_whitespace_end = False
				db("skipped whitespace until ", i, c)

			else:
				continue

		if skip_until_invalid_symbol_char:
			if not is_char_valid_symbol_char(c):
				skip_until_invalid_symbol_char = False
				db("skipped until invalid symbol char found")

			else:
				continue

		if skip_until_valid_symbol_char:
			if is_char_valid_symbol_char(c):
				skip_until_valid_symbol_char = False
				db("skipped until valid symbol char found")

			else:
				continue

		if in_comment_block:
			if contents.startswith('*/', i):
				db("comment block ends at ", i)
				in_comment_block = False

			continue

		else:
			if contents.startswith('/*', i):
				db("comment block starts at ", i)
				in_comment_block = True
				continue

		if contents.startswith('//', i):
			skip_until_newline = True
			continue

		if in_directive:

			db("in_directive")

			for directive in ['include', 'defined', 'if', 'elseif', 'endif', 'emit']:
				if contents.startswith(directive, i):
					skip_until_newline = True
					in_directive = False
					continue

			if contents.startswith('define', i):
				skip_until_whitespace_start = True
				skip_until_whitespace_end = True
				in_directive_define = True
				continue

			if in_directive_define:
				if pos_directive_define == -1:

					# skip constants starting with '_',
					# standard naming convention for internal-only symbols.
					if c == '_':
						in_directive_define = False
						skip_until_newline = True
						continue

					skip_until_whitespace_start = True
					pos_directive_define = i
					db("reached define contents block at ", i, c)

				else:
					final = contents[pos_directive_define:i]

					output_contents += gen_const(final)
					print("[EXTRACTED] DIRECTIVE 'define' DATA: '%s'" % final)

					in_directive = False
					in_directive_define = False
					skip_until_newline = True
					pos_directive_define = -1
					continue

			if c == '\\':
				db("reached newline symbol")
				in_directive = False
				skip_until_newline = True

		else:
			if c == '#':
				in_directive = True
				continue

		if in_function:
			db("in_function")

			# Function name

			if not in_function_declare:
				db("not in function declare (in storage modifier) skipping")
				skip_until_whitespace_end = True
				in_function_declare = True
				continue

			if not data_function_name:
				db("in function name")
				if pos_function_name == -1:
					if not is_char_valid_symbol_char(c):
						db("invalid function name character, skipping until valid")
						skip_until_valid_symbol_char = True
						continue

					if c == '_':
						db("function name begins with _, skipping")
						in_function = False
						in_function_declare = False
						skip_until_newline = True
						continue

					db("reading function name from ", i)
					pos_function_name = i
					skip_until_invalid_symbol_char = True
					continue

				else:
					if c == ':' or c == ' ':
						db("extracted string is tag, starting again")
						pos_function_name = -1
						skip_until_valid_symbol_char = True
						continue

					if c == '(':
						data_function_name = contents[pos_function_name:i]
						pos_function_name = -1
						db("function name '%s'" % data_function_name)

					else:
						db("not a function, skip")
						pos_function_name = -1
						in_function = False
						in_function_declare = False
						skip_until_newline = True
						continue

			# Function parameters

			if not in_function_params and not no_function_params:
				db("reached start of params")

				if not is_char_valid_symbol_char(c):

					if c == ')':
						no_function_params = True

					else:
						continue
					db("invalid symbol character, skipping until valid")

				else:
					in_function_params = True

			if not no_function_params and pos_function_param == -1:
				db("function param start not set")

				if in_function_param_subscript:
					db("in_function_param_subscript")
					if c == '}':
						db("exit parameter subscript block")
						in_function_param_subscript = False

					continue

				else:
					db("not in_function_param_subscript")
					if c == '{':
						db("in parameter subscript block")
						in_function_param_subscript = True
						continue

				if not is_char_valid_symbol_char(c):
					if not in_function_param_subscript:
						if c == '{':
							db("invalid char check: in parameter subscript block")
							in_function_param_subscript = True
							continue

					if contents.startswith('...', i):
						pos_function_param = i
						in_function_param = True

					continue

				pos_function_param = i
				in_function_param = True
				continue

			if in_function_param:
				db("in function param")

				if c == ',' or c == ')':
					data_function_params.append(contents[pos_function_param:i])
					db("parameter found: '%s'" % contents[pos_function_param:i])
					pos_function_param = -1
					in_function_param = False

			if c == ')':
				output_contents += gen_func(data_function_name, data_function_params)
				in_function = False
				print("[EXTRACTED] FUNCTION '%s' PARAMS: %s" % (
					data_function_name, data_function_params))
				continue

		else:
			if (
				contents.startswith('native', i) or
				contents.startswith('forward', i)  # or
				# contents.startswith('stock', i)
			):
				skip_until_whitespace_start = True
				in_function = True
				in_function_params = False
				data_function_name = ""
				data_function_params = []
				no_function_params = False
				continue

	output_contents = output_contents.rstrip("\n,")

	output_contents += """
	]
}
"""

	return output_contents


def process_file(filename):
	"""
	processes a file for outputting extracted contents to a sublime-completions
	file.
	"""

	print(filename)

	contents = ""

	with open(filename, 'r') as input_file:
		contents = input_file.read()

	output_contents = scan_contents(contents)

	with open(filename + '.sublime-completions', 'w') as output_file:
		output_file.write(output_contents)


def main():

	if len(sys.argv) > 1:
		path = sys.argv[1]
	else:
		path = "E:\\Games\\Projects\\SA-MP\\pawno\\include\\autocomplete\\"

	print(path)

	if os.path.isfile(path):
		process_file(path)

	else:
		if not os.path.exists(path):
			print("Directory not found.")
			return

		for f in glob.glob(path + '*.pwn'):
			process_file(f)


if __name__ == '__main__':
	main()
