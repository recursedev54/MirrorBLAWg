import os

os.environ["OPENAI_API_KEY"] = ""


import openai
import tkinter as tk
from tkinter import scrolledtext

class Character:
    def __init__(self, name, tagline, description, greeting, definition):
        self.name = name
        self.tagline = tagline
        self.description = description
        self.greeting = greeting
        self.definition = definition

def generate_response(prompt):
    # Initialize the OpenAI client
    client = openai.Client(api_key=os.environ["OPENAI_API_KEY"])
    
    # Create a chat completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

class CharacterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Character AI")

        # Configure OpenAI client
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
        
        # Character input fields
        self.name_label = tk.Label(root, text="Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        
        self.tagline_label = tk.Label(root, text="Tagline")
        self.tagline_label.pack()
        self.tagline_entry = tk.Entry(root)
        self.tagline_entry.pack()
        
        self.description_label = tk.Label(root, text="Description")
        self.description_label.pack()
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()
        
        self.greeting_label = tk.Label(root, text="Greeting")
        self.greeting_label.pack()
        self.greeting_entry = tk.Entry(root)
        self.greeting_entry.pack()
        
        self.definition_label = tk.Label(root, text="Definition")
        self.definition_label.pack()
        self.definition_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.definition_text.pack()
        
        self.chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.chat_log.pack()
        
        self.message_label = tk.Label(root, text="Your Message")
        self.message_label.pack()
        self.message_entry = tk.Entry(root)
        self.message_entry.pack()
        
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()
        
        self.character = None
        
    def create_character(self):
        name = self.name_entry.get()
        tagline = self.tagline_entry.get()
        description = self.description_entry.get()
        greeting = self.greeting_entry.get()
        definition = self.definition_text.get("1.0", tk.END)
        
        self.character = Character(name, tagline, description, greeting, definition)
        
    def send_message(self):
        if not self.character:
            self.create_character()
        
        user_message = self.message_entry.get()
        self.chat_log.insert(tk.END, f"You: {user_message}\n")
        
        prompt = f"{self.character.name}: {self.character.tagline}\n{self.character.description}\n{self.character.greeting}\n\n{self.character.definition}\nUser: {user_message}\n{self.character.name}:"
        ai_response = generate_response(prompt)
        
        self.chat_log.insert(tk.END, f"{self.character.name}: {ai_response}\n")
        self.message_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterApp(root)
    root.mainloop()




