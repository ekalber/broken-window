import sublime
import re

def check(gem, version):
  if(gem == "rails"):
    description = "Checks for missing JSON encoding (CVE-2015-3226)"
    
    result = re.findall("[0-9]", version)
    
    # Rails 3.x and 4.1.x before 4.1.11 and 4.2.x before 4.2.2 
    if is_reached(result):
      message = "Rails " + version + " does not encode JSON keys (CVE-2015-3226)"
      return message
    else:
      return False
  else:
    return False

def is_reached(version):
  if ((int(version[0]) == 3) or (
        (int(version[0]) == 4) 
        and 
        (
          (
            (int(version[1]) == 1) and (int(version[2]) < 11)
          )
          or
          (
            (int(version[1]) == 2) and (int(version[2]) < 2)  
          )
        )
      )):
    return True
  else:
    return False