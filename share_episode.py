import os
import os.path
import shutil

def run(filename, share_folder):
  """
  Links the given file to the share folder.
  If the `share_folder` and the source file is not on the same device, the file is copied.
  """
  basename = os.path.basename(filename)
  new_file = os.path.join(share_folder, basename)
  if os.path.exists(new_file):
    raise IOError("File already exists: {}".format(basename))

  episode_stats = os.stat(filename)
  share_folder_stats = os.stat(share_folder)

  if episode_stats.st_dev == share_folder_stats.st_dev:
    run_same_device(filename, share_folder)
  else:
    run_different_devices(filename, share_folder)

def run_different_devices(filename, share_folder):
  shutil.copy(filename, new_file)

def run_same_device(filename, share_folder):
  basename = os.path.basename(filename)
  new_file = os.path.join(share_folder, basename)
  os.link(filename, new_file)
