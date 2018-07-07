import sublime
import sublime_plugin


class SequentialNumberInsertCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        value = 0
        for selection in self.view.sel():
            self.view.erase(edit, selection)
            self.view.insert(edit, selection.begin(), str(value))
            value = value + 1
