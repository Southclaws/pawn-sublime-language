import sublime, sublime_plugin
from .edit import Edit

class PawnBuildPathCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().show_input_panel("Set Pawn build path", "C:\\Pawno\\", self.onPawnPathDone, None, None)


	def onPawnPathDone(self, input):
		view = self.view.window().new_file()

		with Edit(view) as edit:
			edit.insert(0,
'{\n\
	"cmd": ["pawncc.exe", "$file", "-o$file_path\\\\\\\\$file_base_name", "-;+", "-(+", "-d3"],\n\
	"file_regex": "(.*?)[(]([0-9]*)[)]",\n\
	"selector": "source.pwn",\n\
	"working_dir": "'+input.replace("\\", "\\\\")+'"\n\
}')

		view.set_name("Pawn.sublime-build")
		view.run_command("save");
