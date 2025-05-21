# import libraries
import pygame
import tkinter as tk
from tkinter import filedialog
import random
import sys
# set class that ask the user to select a quiz file 
class QuizBase:
    def choose_quiz_file(self):
        root = tk.Tk()
        root.withdraw()
        return filedialog.askopenfilename(
            title="Select a quiz file",
            filetypes=[("Text Files", "*.txt")]
        )