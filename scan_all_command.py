import sublime 
import sublime_plugin
from . import broken_window

class ScanAllCommand(sublime_plugin.ApplicationCommand):
  def run(self):
    broken_window.scan_all() 