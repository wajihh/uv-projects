# OpenAI Chatbot

A simple command-line chatbot built with Python that uses OpenAI's GPT-3.5 API to provide interactive conversations.

## Prerequisites

Before you begin, make sure you have:
- Python 3.12 or higher installed
- An OpenAI API key (get one from [OpenAI's website](https://platform.openai.com/api-keys))
- `uv` package manager installed (a faster alternative to pip)

## Project Structure

```
05-chatbot/
├── .env                    # Environment variables (API keys)
├── .gitignore             # Git ignore file
├── .python-version        # Python version specification
├── pyproject.toml         # Project configuration and dependencies
├── README.md              # This file
└── src/
    └── chatbot/           # Main package directory
        ├── __init__.py    # Package initialization
        └── main.py        # Main chatbot implementation
```

## Step-by-Step Setup Guide

1. **Create a new project directory**
   ```bash
   mkdir 05-chatbot
   cd 05-chatbot
   ```

2. **Create a Python virtual environment using uv**
   ```bash
   uv venv
   ```

3. **Activate the virtual environment**
   ```bash
   source .venv/bin/activate  # On Linux/Mac
   # or
   .venv\Scripts\activate     # On Windows
   ```

4. **Create the project structure**
   ```bash
   mkdir -p src/chatbot
   touch src/chatbot/__init__.py
   ```

5. **Create the pyproject.toml file**
   Create a file named `pyproject.toml` with the following content:
   ```toml
   [project]
   name = "05-chatbot"
   version = "0.1.0"
   description = "A chatbot project using OpenAI's API"
   readme = "README.md"
   authors = [
       { name = "Your Name", email = "your.email@example.com" }
   ]
   requires-python = ">=3.12"
   dependencies = [
       "openai>=1.12.0",
       "python-dotenv>=1.0.0",
       "rich>=13.7.0"
   ]

   [project.scripts]
   chatbot = "chatbot.main:main"

   [build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"

   [tool.hatch.build.targets.wheel]
   packages = ["src/chatbot"]
   ```

6. **Create the .env file**
   Create a file named `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

7. **Create the main chatbot implementation**
   Create `src/chatbot/main.py` with the provided code (see the file contents above).

8. **Install the project and its dependencies**
   ```bash
   uv pip install -e .
   ```

## Running the Chatbot

1. **Make sure your virtual environment is activated**
   ```bash
   source .venv/bin/activate  # On Linux/Mac
   # or
   .venv\Scripts\activate     # On Windows
   ```

2. **Run the chatbot**
   ```bash
   chatbot
   ```

3. **Interact with the chatbot**
   - Type your messages and press Enter
   - The chatbot will respond using GPT-3.5
   - Type 'export' to save the current conversation to a Markdown file
   - Type 'exit' to quit the conversation

4. **Exporting Conversations**
   - During the chat, type 'export' at any time to save the conversation
   - The conversation will be saved to a file named `chatbot_conversation_YYYYMMDD_HHMMSS.md`
   - The exported file includes:
     - Conversation date and time
     - All messages exchanged (excluding system messages)
     - Properly formatted Markdown with clear user/assistant distinction

## Common Issues and Solutions

1. **"OPENAI_API_KEY not found" error**
   - Make sure you've created the `.env` file
   - Verify that your API key is correct
   - Ensure the `.env` file is in the project root directory

2. **Package not found errors**
   - Make sure you're in the virtual environment
   - Try reinstalling the package: `uv pip install -e .`

3. **Python version issues**
   - Ensure you're using Python 3.12 or higher
   - Check your Python version: `python --version`

4. **Export file permission issues**
   - Ensure you have write permissions in the current directory
   - Check if the file name is valid for your operating system

## Dependencies

- `openai`: Official OpenAI Python library for API access
- `python-dotenv`: For loading environment variables
- `rich`: For beautiful terminal formatting

## Contributing

Feel free to submit issues and enhancement requests!
