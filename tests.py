from functions.run_python_file import *

print(run_python_file("calculator", "main.py"))
print("")
print(run_python_file("calculator", "tests.py"))
print("")
print(run_python_file("calculator", "../main.py"))
print("")
print(run_python_file("calculator", "nonexistent.py"))