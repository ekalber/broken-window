import sublime
from . import side_bar_linter, status_bar_linter, view_linter

def alert(view, code):
  side_bar_linter.alert(view, code)
  status_bar_linter.alert(view, code)
  view_linter.alert(view, code)