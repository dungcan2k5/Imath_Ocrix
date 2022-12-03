from tkinter import *
from PIL import Image, ImageTk

from app import App
from define import *

window = Tk()
App(window)

# Chọn Loại Chương Trình
choose_ImgOCR = Button(text="Image OCR     |", bg=COLOR_BACKGROUND,         
    borderwidth=0, activebackground=COLOR_BACKGROUND)
choose_ImgOCR.grid(column=0, row=0, sticky=NE, pady=10)

choose_MathOCR = Button(text="   Math OCR", bg=COLOR_BACKGROUND, 
    borderwidth=0, activebackground=COLOR_BACKGROUND)
choose_MathOCR.grid(column=1, row=0, sticky=NW, pady=10)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

mainloop()