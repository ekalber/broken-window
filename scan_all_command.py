import sublime 
import sublime_plugin
from . import broken_window

class scanAllCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    broken_window.scan_view(edit.active_view())