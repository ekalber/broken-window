import sublime 
import sublime_plugin

def alert(view, line, code):
  regs = view.find_all(code, sublime.IGNORECASE, None, None)
  options = sublime.DRAW_SOLID_UNDERLINE|sublime.DRAW_NO_FILL|sublime.DRAW_NO_OUTLINE
  view.add_regions("error"+str(line), regs, "brokenwindow.error","dot", options)

def popup(view, address, message):
  view.show_popup(message, 1, -1, 400, 500, None, None)
