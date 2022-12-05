from tkinter import *
from PIL import Image, ImageTk

from app import App
from define import *

class ScrMath(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent["bg"] = COLOR_BACKGROUND
        
        Label(self, text="Đây là trang 2").grid(row=1)

        self.pack(padx = 10, pady = 10)

