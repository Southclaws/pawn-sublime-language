import sublime, sublime_plugin
from .edit import Edit

class PawnBuildPathCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().show_input_panel("Set Pawn build path", "C:\\Pawno\\", self.onPawnPathDone, None, None)


	def onPawnPathDone(self, path):
		view = self.view.window().new_file()
		path = path.replace("\\", "/")

		with Edit(view) as edit:
			edit.insert(0,"""{
	"cmd": ["pawncc.exe", "$file", "-o$file_path/$file_base_name", "-;+", "-(+", "-d3"],
	"file_regex": "(.*?)\\\\(([0-9]*)[- 0-9]*\\\\)",
	"selector": "source.pwn",
	"working_dir": "%s"
}"""%(path))

		view.set_name("Pawn.sublime-build")
		view.run_command("save");
