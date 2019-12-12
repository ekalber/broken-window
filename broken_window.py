import sublime 
import sublime_plugin
from .lib.analyzers import base_analyzer  

# Perform actions on a view file
def scan_view(view):
  # Archives of a ruby on rails project
  if base_analyzer.is_ruby_file(view): 
    # Just scan the current view     
    base_analyzer.scan(view)

    