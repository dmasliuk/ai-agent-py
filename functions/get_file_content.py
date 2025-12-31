from os import path
from config import MAX_CHARS

def get_file_content(working_directory, file_path):

  working_directory_abs = path.abspath(working_directory)
  target_file = path.normpath(path.join(working_directory_abs, file_path))
  valid_file_path = path.commonpath([working_directory_abs, target_file]) == working_directory_abs
  if not valid_file_path:
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  if not path.isfile(target_file):
    return f'Error: File not found or is not a regular file: "{file_path}"'

  with open(target_file, "r") as f:
    file_content = f.read(MAX_CHARS)
    if f.read(1):
      return f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
  
  return file_content

