# DevAssist

# 🧠 AI Agent Loop with Function Calling

This project implements an **AI agent** capable of reasoning, planning, and tool usage via **function calling** — complete with a feedback loop that enables it to refine its actions based on previous results.

The agent interacts with a set of Python tools (functions) to analyze and manipulate code files based on natural language instructions from the user. It iteratively refines its understanding and actions through multiple calls to the LLM until it achieves the goal or reaches a maximum iteration limit.

---

## 🚀 Features

✅ Conversational agent loop with LLM feedback  
🔁 Iterative reasoning and planning based on conversation history  
🛠️ Dynamic function calling (tool use) with schema validation  
📁 Modular design with all tools and schemas organized in `functions/`  
🧪 Example use-case: Bug fixing and understanding how a calculator renders results  
💬 Full traceability of the agent's decisions and tool interactions  

---

## 🧠 Agent Workflow

### 1. Initialization:
- User provides a natural language instruction  
  _Example:_ `"Fix the bug in the calculator"`

### 2. Agent Plans:
- The LLM chooses which tool/function to call based on the user prompt.

### 3. Function Call:
- The selected tool is invoked via `call_function.py`, which:
  - Validates arguments using its schema
  - Executes the function safely
  - Catches and logs exceptions

### 4. Tool Response:
- The function result is wrapped as a message (`role="tool"`) and added to the conversation.

### 5. Looping:
- The LLM re-evaluates its next step using the **entire conversation history**, and:
  - May call another function
  - May update its internal plan
  - Repeats until:
    - A satisfactory response is returned, or
    - The iteration limit (20) is reached

### 6. Final Output:
- The final answer is printed for the user
- The loop terminates cleanly

---

## 🧰 Available Tools

Each tool is defined as a **separate Python file** in the `functions/` directory, with:
- A function implementation
- A schema (`tool_schema`) compatible with the Gemini (or OpenAI) function-calling format

### Example Tools

| Tool Name         | Description                            |
|------------------|----------------------------------------|
| `get_files_info` | Lists files in a directory             |
| `get_file_content` | Reads the contents of a file         |
| `write_file`     | Overwrites a file with new content     |
| `run_python_file`| Executes a Python script and returns output |

> ✅ You can easily extend this system by adding new tools to `functions/`, following the same structure.

---


