import sublime
import sublime_plugin
from . import side_bar_linter, status_bar_linter, view_linter

def alert(view, line, code, message):
  status_bar_linter.alert(view, line, message)
  view_linter.alert(view, line, code)
  view_linter.popup(view, code, message) 

def side_bar_alert():
  side_bar_linter.alert()  

def side_bar_clear():
  side_bar_linter.clear()