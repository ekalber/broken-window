import os
import sublime 
import sublime_plugin
from .lib.analyzers import base_analyzer  

# Perform actions on a view file
def scan_view(view):
  # Archives of a ruby on rails project
  if base_analyzer.is_ruby_file(view): 
    # Just scan the current view     
    base_analyzer.scan(view)

# Perform actions on all views
def scan_all():
  path = sublime.active_window().folders()[0]
  
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
    for file in f:
      if ('.rb' in file) or ('.html.erb' in file) or ('Gemfile' in file):
        files.append(os.path.join(r, file))

  for f in files: 
    scan_view(sublime.active_window().open_file(f, sublime.TRANSIENT))