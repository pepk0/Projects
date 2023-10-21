import tkinter as tk
from Wordy.utils.functionality import validate_words
from tkinter import ttk

class App(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.title = "Wordy"
        self.geometry("700x200")
        self.resizable(False, False)

        label_frame = tk.LabelFrame(
            self, text="Found Words", height=74, labelanchor="n",
            borderwidth=4, font=("Helvetica", 16), border=3)

        sentence_entry = tk.Entry(
            label_frame, width=60, font=("Helvetica", 14),
            bg="systembuttonface", bd=0)

        label_frame.pack(pady=20)
        sentence_entry.pack(pady=20)