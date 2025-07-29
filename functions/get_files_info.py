import os
from google.genai import types


def get_files_info(working_directory, directory = "."):
    working_directory = os.path.abspath(working_directory)
    directory = os.path.join(working_directory, directory)
    directory = os.path.abspath(directory)

    if not directory.startswith(working_directory):
        return (f"Error: Cannot list '{directory}' as it is outside the permitted working directory")
    if not os.path.isdir(directory):
        return f"Error: '{directory}' is not a directory"
    
    try:
        contents = os.listdir(directory)
        return_array = []
        for content in contents:
            filename = content
            file_size = os.path.getsize(directory + "/" + filename)
            is_dir = os.path.isdir(directory + "/" + filename)
            return_array.append(f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}")
        string = "\n".join(return_array)
        return string
    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
