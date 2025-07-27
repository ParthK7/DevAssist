import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

if len(sys.argv) < 2:
    print("Please provide a prompt to get a response")
    sys.exit(1)
else:
    prompt = sys.argv[1]
    messages = [
        types.Content(role = "user", parts = [types.Part(text = prompt)]),
    ]


response = client.models.generate_content(
    model = "gemini-2.0-flash-001", 
    contents = messages, 
    config = types.GenerateContentConfig(tools = [available_functions], system_instruction = system_prompt)
)


if sys.argv[-1] == "--verbose":
    print(f"User prompt: {prompt}")
    print(f"LLM response:- \n {response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

else:
    if not response.function_calls:
        print (f"LLM response:- \n {response.text}")
    
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    