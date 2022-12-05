from tkinter import *
from PIL import Image, ImageTk
import keyboard


from define import *
from img_OCR_func import *
from snip_screen import file_name


class ScrImg(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        def showText():
            text = detect_text()
            showTextLabel.config(state="normal")
            showTextLabel.delete('1.0', END)
            showTextLabel.insert("end",text)
            showTextLabel.config(state="disabled")

            # Image is Captured
            im = Image.open(f"Img_temp/{file_name}.png").resize((425, 50), Image.Resampling.LANCZOS)
            imgCapScr = ImageTk.PhotoImage(im)
            showImgLabel = Label(self, image=imgCapScr)
            showImgLabel.image = imgCapScr
            showImgLabel.grid(column=0, row=0, sticky=NSEW, padx=20)

        # Show Image
        showImgLabel = Text(self, bg="light yellow", height=20)
        showImgLabel.grid(column=0, row=0, sticky=NSEW, padx=20)

        # Show Text
        showTextLabel = Text(self, bg="white", height=20)
        showTextLabel.grid(column=1, row=0, sticky=NSEW, padx=20)

        # Icon For Button
        icoSnipScr = ImageTk.PhotoImage(Image.open("icon/snip_screen.png").resize((30, 30), Image.Resampling.LANCZOS))
        
        # Snip Screen Button
        btnSnipScr = Button(self, image=icoSnipScr, text="Chụp ảnh màn hình", width=190, height=40, compound="left", command=showText)
        btnSnipScr.image = icoSnipScr
        btnSnipScr.grid(column=0, row=1)


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        parent["bg"] = COLOR_BACKGROUND

        self.pack(padx = 10, pady = 10)