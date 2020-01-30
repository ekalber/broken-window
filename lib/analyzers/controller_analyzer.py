import sublime
import sublime_plugin

def scan(view):
  main_region = sublime.Region(0, view.size())
  regions = view.lines(main_region)
  line_number = 0
  for region in regions:
    line_number += 1
    if not region.empty():
      view.erase_regions("error"+str(line_number))
      line = view.substr(region)
      
      warn = forgery_setting_checker.check(line)

      if warn:
        base_linter.alert(view, line_number, line, warn)