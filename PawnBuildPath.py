import json
import sublime
import sublime_plugin
from .edit import Edit


class PawnBuildPathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel(
            "Working directory that contains pawncc.exe",
            "C:\\Pawno\\",
            self.onPawnPathDone,
            None,
            None
        )

    def onPawnPathDone(self, path):
        view = self.view.window().new_file()
        path = path.replace("\\", "/")

        obj = {
            "cmd": [
                "pawncc.exe",
                "$file",
                "-o$file_path/$file_base_name",
                "-;+",
                "-(+",
                "-d3"
            ],
            "file_regex": r"(.*?)\(([0-9]*)[- 0-9]*\)",
            "selector": "source.pwn",
            "working_dir": path
        }

        with Edit(view) as edit:
            edit.insert(0, json.dumps(obj, indent=4))

        view.set_name("Pawn.sublime-build")
        view.run_command("save")
