import tkinter as tk
from tkinter import messagebox
import random
import nltk
from nltk.corpus import brown
import pyperclip

class FrogLevelGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Frog Level Game")
        
        # Seed the random number generator for reproducibility
        random.seed(42)
        
        self.colors = []
        self.word_pairs = []
        self.current_level = 0

        self.lexicon = self.load_lexicon()

        self.title_screen()
    
    def load_lexicon(self):
        # Download the Brown corpus if not already downloaded
        nltk.download('brown')
        # Load the Brown corpus
        brown_freqs = nltk.FreqDist(brown.words())
        # Get the most common words along with their frequencies
        most_common_words = brown_freqs.most_common(1000)  # Adjust the number as needed
        lexicon = [word for word, _ in most_common_words]
        return lexicon

    def title_screen(self):
        self.clear_screen()
        
        self.canvas = tk.Canvas(self.root, width=600, height=300)
        self.canvas.pack()

        self.canvas.create_rectangle(50, 50, 250, 250, fill="magenta", tags="color1")
        self.canvas.create_rectangle(350, 50, 550, 250, fill="lime", tags="color2")
        
        self.canvas.create_text(300, 150, text="Frog Level", font=("Helvetica", 24))

        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack(pady=20)
    
    def start_game(self):
        self.clear_screen()
        self.canvas = tk.Canvas(self.root, width=600, height=300)
        self.canvas.pack()

        self.level_label = tk.Label(self.root, text=f"Level: {self.current_level + 1}", font=("Helvetica", 14))
        self.level_label.pack()

        self.word_pair_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.word_pair_label.pack()

        self.label1 = tk.Label(self.root, text="")
        self.label1.pack(side=tk.LEFT, padx=10)
        
        self.label2 = tk.Label(self.root, text="")
        self.label2.pack(side=tk.LEFT, padx=10)
        
        self.button1 = tk.Button(self.root, text="Next Level", command=lambda: self.check_guess("color1"))
        self.button1.pack(side=tk.LEFT, padx=10)
        
        self.button2 = tk.Button(self.root, text="Next Level", command=lambda: self.check_guess("color2"))
        self.button2.pack(side=tk.LEFT, padx=10)
        
        self.add_new_colors()
        self.show_colors()
    
    def add_new_colors(self):
        color1 = self.generate_random_color()
        color2 = self.generate_random_color()
        self.colors.append(color1)
        self.colors.append(color2)
        self.word_pairs.append(self.generate_random_word_pair())
    
    def generate_random_color(self):
        color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return {"name": color, "hex": color}
    
    def show_colors(self):
        self.canvas.delete("all")
        color1 = self.colors[self.current_level * 2]
        color2 = self.colors[self.current_level * 2 + 1]
        
        hint_color = random.choice([color1, color2])  # Choose one color for the hint
        
        self.canvas.create_rectangle(50, 50, 250, 250, fill=color1["name"], tags="color1")
        self.canvas.create_rectangle(350, 50, 550, 250, fill=color2["name"], tags="color2")
        
        self.canvas.create_text(150, 280, text=f"Hex Code: {hint_color['hex']}", font=("Helvetica", 12), tags="hint_text")
        
        self.level_label.config(text=f"Level: {self.current_level + 1}")
        self.word_pair_label.config(text=self.word_pairs[self.current_level])
    
    def generate_random_word_pair(self):
        return random.choice(self.lexicon)
    
    def check_guess(self, selected_color):
        color1 = self.colors[self.current_level * 2]
        color2 = self.colors[self.current_level * 2 + 1]

        if selected_color == "color1":
            if color1["name"] == self.colors[self.current_level * 2]["name"]:
                self.current_level += 1
                self.add_new_colors()
                self.show_colors()
                self.canvas.itemconfig("color1", fill="green")
                self.canvas.after(500, lambda: self.canvas.itemconfig("color1", fill=color1["name"]))
                self.canvas.after(1000, lambda: self.flash_screen("True"))
            else:
                self.canvas.itemconfig("color1", fill="red")
                self.canvas.after(500, lambda: self.canvas.itemconfig("color1", fill=color1["name"]))
                self.canvas.after(1000, lambda: self.flash_screen("False"))
                messagebox.showinfo("Incorrect Guess", "Please click on the correct hex code.")
        elif selected_color == "color2":
            if color2["name"] == self.colors[self.current_level * 2 + 1]["name"]:
                self.current_level += 1
                self.add_new_colors()
                self.show_colors()
                self.canvas.itemconfig("color2", fill="green")
                self.canvas.after(500, lambda: self.canvas.itemconfig("color2", fill=color2["name"]))
                self.canvas.after(1000, lambda: self.flash_screen("True"))
            else:
                self.canvas.itemconfig("color2", fill="red")
                self.canvas.after(500, lambda: self.canvas.itemconfig("color2", fill=color2["name"]))
                self.canvas.after(1000, lambda: self.flash_screen("False"))
                messagebox.showinfo("Incorrect Guess", "Please click on the correct hex code.")

    def copy_to_clipboard(self, color_hex):
        pyperclip.copy(color_hex)

    def flash_screen(self, result):
        flash_label = tk.Label(self.root, text=result, font=("Helvetica", 36), bg="white")
        flash_label.place(relx=0.5, rely=0.5, anchor="center")
        self.root.after(500, flash_label.destroy)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = FrogLevelGame(root)
    root.mainloop()
