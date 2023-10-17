from utitis.functinality import make_sentence
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Random sentence generator")
        self.geometry("690x180")
        self.resizable(False, False)
        self.iconbitmap(r"RandomSentencesGenerator\img\dice.ico")

        # method to generate the text from a function and place it
        # on the output frame
        def get_sentence() -> None:
            sentence = make_sentence()
            sentence_entry.delete(0, tk.END)
            sentence_entry.insert(0, sentence)

        # method to cleat the output bar
        def clear() -> None:
            sentence_entry.delete(0, tk.END)

        label_frame = tk.LabelFrame(
            self, text="🔽Random Sentence🔽", height=74, labelanchor="n",
            borderwidth=4, font=("Helvetica", 16), border=3)

        sentence_entry = tk.Entry(
            label_frame, width=60, font=("Helvetica", 14),
            bg="systembuttonface", bd=0)

        # frame for button placement
        button_frame = tk.Frame(self)

        randomize_button = ttk.Button(
            button_frame, text="Randomize", width=20,
            command=get_sentence)

        clear_button = ttk.Button(button_frame, text="Clear", command=clear)

        # placing all the widgets
        label_frame.pack(pady=20)
        sentence_entry.pack(pady=20, padx=5)
        button_frame.pack(pady=5)
        randomize_button.grid(row=0, column=0)
        clear_button.grid(row=0, column=1)
