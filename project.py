import tkinter as tk
from tkinter import messagebox
from gtts import gTTS 
import os

def play_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            tts = gTTS(text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "open output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("(Warning)", "Please enter some text:")

def clear_text():
    text_entry.delete("1.0", tk.END)

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("600x400")  # Changed window size

# Change background color of the window
root.config(bg="white")

# Create a text entry widget with modified font, color, and size
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40, font=("Arial", 12), bg="white", fg="gray")
text_entry.pack(pady=15)

# Create buttons with modified font, color, and size
play_button = tk.Button(root, text="Run", command=play_text, font=("Arial", 14), bg="blue", fg="white", width=17, height=2)
play_button.pack(pady=10)

set_button = tk.Button(root, text="Clear", command=clear_text, font=("Arial", 14), bg="blue", fg="white", width=17, height=2)
set_button.pack(pady=10)

exit_button = tk.Button(root, text="out", command=exit_app, font=("Arial", 14), bg="blue", fg="white", width=17, height=2)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
