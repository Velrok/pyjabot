import os
import re

def extract_meta_data(filepath):
  pattern_parts = [
      "(?P<showname>[\w\(\) ]*)",
      " - S?(?P<s_nr>\d*)[xeE]?(?P<ep_nr>\d*)",
      "( - ([^-]*))?",
      "( - ([^-]*))?",
      "(.*)",
      "\.(?P<ext>\w+)"]
  pattern  = re.compile("".join(pattern_parts))
  filename = os.path.basename(filepath)

  match = pattern.search(filename)
  if match:
    season_nr  = None
    episode_nr = None
    try:
      season_nr = int(match.group("s_nr"))
    except ValueError:
      pass
    try:
      episode_nr = int(match.group("ep_nr"))
    except ValueError:
      pass
    return { "ext"      : match.group("ext"),
             "season#"  : season_nr,
             "episode#" : episode_nr,
             "showname" : match.group("showname") }
  else:
    return None

def list(shows_path):
  all_files = os.walk(shows_path)
  leaf_tripple = filter(
      lambda t: len(t[2]) > 0,
      all_files)

  meta_data = []
  for path, dirs, files in leaf_tripple:
    for f in files:
      filepath = os.path.join(path, f)
      meta     = extract_meta_data(filepath)
      result   = {"filepath": filepath}

      if meta:
        result.update(meta)
      meta_data.append(result)

  return meta_data
