import os

def write_file(working_directory, file_path, content):
    working_directory = os.path.abspath(working_directory)
    file_path = os.path.join(working_directory, file_path)
    file_path = os.path.abspath(file_path)

    if not file_path.startswith(working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    with open(file_path, "w") as f:
        f.write(content)
    print (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')


