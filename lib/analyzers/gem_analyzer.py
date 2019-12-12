import sublime
import re
from ...lib.checkers import json_encoding_checker 
from ...lib.linters import base_linter 

def scan(view):
  # Por cada línea llamar a los checks que se crea conveniente
  for i, line in enumerate(open(view.file_name())):    
    result = re.findall("\"(.*?)\"", line)
    
    if result:
      name = result[0].replace('"', '')
      version = result[1]

      if (name != "") and (version != ""):
        warn = json_encoding_checker.check(name, version)

        if warn:
          base_linter.alert(view, warn)