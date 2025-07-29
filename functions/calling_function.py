import os 
from google.genai import types

from functions.get_file_content import *
from functions.get_files_info import *
from functions.run_python_file import *
from functions.write_file import *

function_dictionary = {
    "get_file_content" : get_file_content,
    "get_files_info" : get_files_info,
    "run_python_file" : run_python_file,
    "write_file" : write_file
}

def call_function(function_call_part, verbose = False):
    if verbose:
        print(f" - Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    if function_call_part.name not in function_dictionary:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    func = function_dictionary[function_call_part.name]
        

    args = function_call_part.args
    args["working_directory"] = "./calculator"

    function_result = func(**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name = function_call_part.name,
                response={"result": function_result},
            )
        ],
    )

    