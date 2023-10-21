import tkinter as tk
from utils.functionality import validate_words
from tkinter import ttk

class App(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.title = "Wordy"
        self.geometry("700x200")
        self.resizable(False, False)

        label_frame = tk.LabelFrame(
            self, text="", height=74, labelanchor="n",
            borderwidth=4, font=("Helvetica", 16), border=3)
        
        label_frame.pack()