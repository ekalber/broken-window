import sublime
import re
from os.path import normpath, basename
from . import gem_analyzer, controller_analyzer, model_analyzer, view_analyzer

# It is set if it is a ruby file or a gem file
def is_ruby_file(view):
  try:
    if view.window().extract_variables()['file_extension'] == 'rb':
      return True
    if view.window().extract_variables()['file_extension'] == 'html.erb':
      return True
    elif view.window().extract_variables()['file_name'] == "Gemfile":
      return True
    else:
      return False
  except:
    return False

# Define what type of file is within the Ruby on Rails project to 
# bring down the corresponding analysis module
def scan(view):
  if view.window().extract_variables()['file_name'] == "Gemfile":
    gem_analyzer.scan(view)
  else:
    file_path_name = file_path(view)
    if file_path_name == "controllers":
      controller_analyzer.scan(view)
    elif file_path_name == "models":
      model_analyzer.scan(view)
    elif file_path_name == "views":
      view_analyzer.scan(view) 
    else:
      return False

# Return the folder inside the project
def file_path(view):
  try:
    return basename(normpath(view.window().extract_variables()['file_path']))
  except:
    return ""