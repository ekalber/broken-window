import sublime

def alert():
  changes = {
    "show_git_status": False,
    "theme": "BrokenWindow.sublime-theme",
    "color_scheme": "Packages/BrokenWindow/Default.sublime-color-scheme"
  }

  base_settings = sublime.load_settings('Preferences.sublime-settings')
  for key, value in changes.items():
    base_settings.set(key, value)
  sublime.save_settings('Preferences.sublime-settings')

def clear():
  changes = {
    "show_git_status": False,
    "theme": "Default.sublime-theme"
  }

  base_settings = sublime.load_settings('Preferences.sublime-settings')
  for key, value in changes.items():
    base_settings.set(key, value)
  sublime.save_settings('Preferences.sublime-settings')