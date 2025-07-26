import os
import subprocess

def run_python_file(working_directory, file_path, args = None):
    rel_file_path = file_path
    working_directory = os.path.abspath(working_directory)
    file_path = os.path.join(working_directory, file_path)
    file_path = os.path.abspath(file_path)

    if not file_path.startswith(working_directory):
        return f'Error: Cannot execute "{rel_file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        return f'Error: File "{rel_file_path}" not found'
    if not os.path.splitext(file_path)[1] == ".py":
        return f'Error: "{rel_file_path}" is not a Python file.'
    
    try:
        commands = ["python3", f"{file_path}"]
        if args:
            commands.extend(args)
        result  = subprocess.run(commands, capture_output = True, timeout = 30)
        return_array = []
        return_array.append(f"STDOUT: {result.stdout}")
        return_array.append(f"STDERR: {result.stderr}")
        if result.returncode != 0:
            return_array.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            return_array.append(f"No output produced")
        
        result_string = "\n".join(return_array)
        return result_string
    except Exception as e:
        return f"Error executing python file : {e}"

