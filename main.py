import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions
from functions.calling_function import *

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

verbose = "--verbose" in sys.argv

args = []
for arg in sys.argv[1:]:
    if not arg.startswith("--"):
        args.append(arg)

if not args:
    print ("Please provide a prompt to get a response")
    print("Examples:-")
    print("python3 main.py 'What are the contents of main.py?'")
    sys.exit(1)
else:
    prompt = " ".join(args)
    messages = [
        types.Content(role = "user", parts = [types.Part(text = prompt)]),
    ]

iterations = 0

try:
    while iterations <= 20:
        response = client.models.generate_content(
            model = "gemini-2.0-flash-001", 
            contents = messages, 
            config = types.GenerateContentConfig(tools = [available_functions], system_instruction = system_prompt)
        )

        for candidate in response.candidates:
            messages.append(candidate.content)

        if verbose:
            # print(f"User prompt: {prompt}")
            # print(f"LLM response:- \n {response.text}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if not response.function_calls:
            # print("No function call detected")
            print (f"LLM response:- \n {response.text}")
            break
            # print("The function you want to perform is not specified")
            # sys.exit(0)

        function_responses = []
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)
            if (
                not function_call_result.parts
                or not function_call_result.parts[0].function_response.response
            ):
                raise Exception ("Empty result for function call")
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            function_responses.append(function_call_result.parts[0])

        for tool_response in function_responses:
            new_message = types.Content(role = "tool", parts = [tool_response])
            messages.append(new_message)
        
        iterations += 1

        
except Exception as e:
    print(f"Error occured: {e}")
    sys.exit(1)