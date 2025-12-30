from os import path
from os import listdir

def get_files_info(working_directory, directory = "."):

    working_directory_abs = path.abspath(working_directory)
    target_dir = path.normpath(path.join(working_directory_abs, directory))
    valid_target_dir = path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not isinstance(directory, str):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    total_info = ""
    for item in listdir(target_dir):
        item_path = path.join(target_dir, item)
        is_dir = path.isdir(item_path)
        total_info = total_info + f"- {item}: file_size={path.getsize(item_path)} bytes, is_dir={is_dir}\n"

    return total_info
