import sublime 
import sublime_plugin
from . import broken_window

class BrokenWindowEvents(sublime_plugin.EventListener): 
  # Called after changes have been made to a view
  def on_modified_async(self, view):
    # If there is any change in the buffer without saving
    if view.is_dirty() == True:
      broken_window.scan_view(view)    

  # Called when a view gains input focus
  def on_activated_async(self, view):
    broken_window.scan_view(view)

  # Called after a view has been saved
  def on_post_save_async(self, view):
    broken_window.scan_view(view)
 
  # Called when the file is finished loading
  def on_load_async(self, view):
    broken_window.scan_view(view)