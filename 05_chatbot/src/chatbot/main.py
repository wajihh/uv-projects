import os
from typing import List
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def export_conversation(messages: List[dict], filename: str):
    """Export the conversation to a Markdown file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Chatbot Conversation\n\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for msg in messages:
            if msg["role"] == "system":
                continue
            role = "You" if msg["role"] == "user" else "Assistant"
            f.write(f"## {role}\n\n")
            f.write(f"{msg['content']}\n\n")

def main():
    load_dotenv()
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    if not os.getenv("OPENAI_API_KEY"):
        console.print("[red]Error: OPENAI_API_KEY not found in environment variables[/red]")
        return
    
    console.print("[bold blue]Welcome to the Chatbot![/bold blue]")
    console.print("Type 'exit' to quit the conversation.")
    console.print("Type 'export' to save the conversation to a Markdown file.\n")
    
    messages: List[dict] = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]
    
    while True:
        user_input = console.input("[bold green]You:[/bold green] ")
        
        if user_input.lower() == "exit":
            break
            
        if user_input.lower() == "export":
            filename = f"chatbot_conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            export_conversation(messages, filename)
            console.print(f"[green]Conversation exported to {filename}[/green]")
            continue
            
        messages.append({"role": "user", "content": user_input})
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            
            assistant_message = response.choices[0].message.content
            messages.append({"role": "assistant", "content": assistant_message})
            
            console.print("\n[bold blue]Assistant:[/bold blue]")
            console.print(Markdown(assistant_message))
            console.print()
            
        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/red]")

if __name__ == "__main__":
    main() 