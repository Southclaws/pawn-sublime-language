import sublime, sublime_plugin
import webbrowser

class OpenWikiOnString(sublime_plugin.TextCommand):

	def run(self, edit):
		query = self.view.substr(self.view.sel()[0])
		webbrowser.open_new("http://wiki.sa-mp.com/wiki/" + query)
