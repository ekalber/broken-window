import sublime 

def alert(view, code):
    view.add_regions(code, view.find_all(code, sublime.IGNORECASE, None, None), "somescope","Packages/HolaMundo/icons/test.png", sublime.DRAW_SOLID_UNDERLINE|sublime.DRAW_NO_FILL|sublime.DRAW_NO_OUTLINE)