import tkinter as tk
from tkinter import filedialog, Text
import os
import glob

class FakeIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake IDE")
        self.root.attributes('-fullscreen', True)  # Set window to fullscreen
        self.root.configure(bg="black")

        self.text_area = Text(self.root, bg="white", fg="black", insertbackground="black")
        self.text_area.pack(expand=1, fill='both')

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New File", command=self.new_file)
        self.file_menu.add_command(label="Load Text File", command=self.load_text_file_dialog)
        self.file_menu.add_command(label="Save File", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=lambda: self.text_area.event_generate("<<Undo>>"))
        self.edit_menu.add_command(label="Redo", command=lambda: self.text_area.event_generate("<<Redo>>"))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))

        self.exit_button = tk.Button(self.root, text="X", command=self.root.destroy, bg="red", fg="white")
        self.exit_button.pack(anchor="ne", padx=10, pady=10)

        self.load_all_txt_files()

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def load_text_file_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.load_text_file(file_path)

    def load_text_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def load_all_txt_files(self):
        txt_files = sorted(glob.glob("*.txt"), key=os.path.getmtime)
        all_content = ""
        for file_path in txt_files:
            with open(file_path, "r") as file:
                all_content += file.read() + "\n"
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(1.0, all_content)

if __name__ == "__main__":
    root = tk.Tk()
    ide = FakeIDE(root)
    root.mainloop()
