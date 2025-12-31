from os import path
from os import makedirs

def write_file(working_directory, file_path, content):

  working_directory_abs = path.abspath(working_directory)
  target_file = path.normpath(path.join(working_directory_abs, file_path))
  valid_file_path = path.commonpath([working_directory_abs, target_file]) == working_directory_abs
  if not valid_file_path:
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
  if path.isdir(target_file):
    return f'Error: Cannot write to "{file_path}" as it is a directory'
  
  makedirs(target_file.replace(file_path, ""), exist_ok=True)

  with open(target_file, "w") as f:
    f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  