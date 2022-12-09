from tkinter import *
from PIL import Image, ImageTk, ImageGrab
import time, pyperclip

from app import App
from define import *
from snip_screen import snip_screen
from snip_screen import file_name

class ScrMath(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent["bg"] = COLOR_BACKGROUND
        self["bg"] = COLOR_BACKGROUND
        self.pack(padx = 10, pady = 10)

        def show_image():
            pass


        # Show Image
        showImgLabel = Text(self, bg="light yellow", height=6)
        showImgLabel.grid(columnspan=2, row=0, sticky=NSEW, pady=10)

        # Show Text
        showTextLabel = Text(self, bg="white", height=6)
        showTextLabel.grid(columnspan=2, row=1, sticky=NSEW, pady=10)

        # Show Latex
        showLatexLabel = Text(self, bg="white", height=1, font=("Arial", 14))
        showLatexLabel.grid(columnspan=2, row=2, sticky=NSEW, pady=10)

        # Icon For Snip Screen Button
        icoSnipScr = ImageTk.PhotoImage(Image.open("icon/snip_screen.png").resize((30, 30), Image.Resampling.LANCZOS))
        
        # Snip Screen Button
        btnSnipScr = Button(self, image=icoSnipScr, text="Chụp ảnh màn hình", width=190, height=40, compound="left", command=show_image)
        btnSnipScr.image = icoSnipScr
        btnSnipScr.grid(column=0, row=3, pady=10)

        # Icon Copy To Clipboard
        icoClipboard = ImageTk.PhotoImage(Image.open("icon/icon_clipboard.png").resize((30, 30), Image.Resampling.LANCZOS))

        # Copy Content To Clipboard
        btnCopy = Button(self, image=icoClipboard, text="Sao chép vào bộ nhớ tạm", width=190, height=40, compound="left")
        btnCopy.image = icoClipboard
        btnCopy.grid(column=1, row=3, pady=10)        

        # Thiết đặt kích thước cách cột trong khung hinh
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

