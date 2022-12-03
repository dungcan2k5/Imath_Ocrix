from tkinter import *
from PIL import Image, ImageTk

from app import App
from define import *


class ScrMath():
    def __init__(self, window) -> None:

        # Open Img_OCR Screen
        def openImgScr():
            window.destroy()

        window = Tk()
        App(window)
        
        # Chọn Loại Chương Trình
        choose_ImgOCR = Button(window, text="Image OCR     |", bg=COLOR_BACKGROUND, borderwidth=0, activebackground=COLOR_BACKGROUND, command=openImgScr)
        choose_ImgOCR.grid(column=0, row=0, sticky=NE, pady=10)

        choose_MathOCR = Button(window, text="   Math OCR", bg=COLOR_BACKGROUND, 
            borderwidth=0, activebackground=COLOR_BACKGROUND)
        choose_MathOCR.grid(column=1, row=0, sticky=NW, pady=10)

        Label(window, text="Đây là trang 2").grid(row=1)

        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
