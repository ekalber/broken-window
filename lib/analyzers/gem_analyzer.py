import sublime
import sublime_plugin
import re
from ...lib.checkers import json_encoding_checker 
from ...lib.linters import base_linter 

def scan(view):
  # All code from a view to a main region for obtain regions
  main_region = sublime.Region(0, view.size())
  # Lines of view to regions
  regions = view.lines(main_region)
  line_number = 0
  error = False

  # Iterate regions
  for region in regions:
    line_number += 1
    # If line not empty
    # Por cada línea llamar a los checks que se crea conveniente
    if not region.empty():
      # Se eliminan las alertas de error anteriores
      view.erase_regions("error"+str(line_number))
      #
      
      line = view.substr(region)
      
      result = re.findall("[\"-\'](.*?)[\"-\']", line)
    
      if result:
        try:
          name = result[0].replace('"', '').replace("'", "")
          version = result[1]
        except:
          name = ""
          version = ""

        if (name != "") and (version != ""):
          warn = json_encoding_checker.check(name, version)

          if warn:
            error = True
            base_linter.alert(view, line_number, line, warn)

  if error:
    base_linter.side_bar_alert()
  else:
    base_linter.side_bar_clear()


def scan_gemfile(name, version):
  # Por cada línea llamar a los checks que se crea conveniente
  # All code from a view to a main region for obtain regions
  main_region = sublime.Region(0, view.size())
  # Lines of view to regions
  regions = view.lines(main_region)
  line_number = 0
  # Iterate regions
  for region in regions:
    line_number += 1
    # If line not empty
    # Por cada línea llamar a los checks que se crea conveniente
    if not region.empty():
      # Se eliminan las alertas de error anteriores
      view.erase_regions("error"+str(line_number))

      line = view.substr(region)
      
      result = re.findall("[\"-\'](.*?)[\"-\']", line)
    
      if result:
        name = result[0].replace('"', '').replace("'", "")
        version = result[1]

        if (name != "") and (version != ""):
          warn = json_encoding_checker.check(name, version)

          if warn:
            base_linter.alert(view, line_number, line, warn)
    
    