import sublime 
import sublime_plugin

def alert(view, line, message):
  view.window().status_message(message + " (Line: " + str(line) + ")")