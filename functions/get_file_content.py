import os
from google.genai import types

def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    file_path = os.path.join(working_directory, file_path)
    file_path = os.path.abspath(file_path)

    if not file_path.startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        MAX_CHARS = 10000

        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(file_path) > MAX_CHARS:
                file_content_string += f'\n [...File "{file_path}" truncated at 10000 characters]'
        return file_content_string 
    except Exception as e:
        return f"Error reading file contents {file_path} : {e}"

schema_get_file_content = types.FunctionDeclaration(
    name = "get_file_content", 
    description = "List the contents of the specified file if it exists and is within the given working directory. The output is limited to 10000 characters.", 
    parameters = types.Schema(
        type = types.Type.OBJECT, 
        properties = {
            "file_path" : types.Schema(
                type = types.Type.STRING,
                description = "The path of the file, relative to the working directory."
            ),
        },
    ),
)