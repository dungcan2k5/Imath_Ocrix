from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import requests
import time


from define import *
from img_OCR_func import *
from snip_screen import file_name


class ScrImg(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self["bg"] = COLOR_BACKGROUND
        self.pack(padx = 10, pady = 10)

        def inputUriBox():

            UrlInputBox = Toplevel()
            content = Entry(UrlInputBox)
            content.pack()
            uri = content.get()
            while(len(uri) == 0):
                time.sleep(1.5)
                uri = content.get()

            def click():
               UrlInputBox.distroy()
                

            Button(UrlInputBox, text="OK", command=click).pack()
            
            text = detect_text_uri(uri)
            showTextLabel.config(state="normal")
            showTextLabel.delete('1.0', END)
            showTextLabel.insert("end", text)
            showTextLabel.config(state="disabled")

            response = requests.get(uri)
            img = Image.open(BytesIO(response.content))
            height = round(425 * (img.height / img.width))
            resized = img.resize((425, height), Image.Resampling.LANCZOS)
            imgUri = ImageTk.PhotoImage(resized) 

            showImgLabel.config(state="normal")
            showImgLabel.delete('1.0', END)
            showImgLabel.image_create(END, image=imgUri)
            showImgLabel.image = imgUri
            showImgLabel.config(state="disabled")           

        def showText():
            text = detect_text()
            showTextLabel.config(state="normal")
            showTextLabel.delete('1.0', END)
            showTextLabel.insert("end", text)
            showTextLabel.config(state="disabled")

            # Image is Captured
            im = Image.open(f"Img_temp/{file_name}.png")
            height = round(425 * (im.height / im.width))
            resized = im.resize((425, height), Image.Resampling.LANCZOS)
            imgCapScr = ImageTk.PhotoImage(resized)

            showImgLabel.config(state="normal")
            showImgLabel.delete('1.0', END)
            showImgLabel.image_create(END, image=imgCapScr)
            showImgLabel.image = imgCapScr
            showImgLabel.config(state="disabled")

        # Show Image
        showImgLabel = Text(self, bg="light yellow", height=20)
        showImgLabel.grid(columnspan=2, row=0, sticky=NSEW, padx=10)

        # Show Text
        showTextLabel = Text(self, bg="white", height=20)
        showTextLabel.grid(column=2, row=0, sticky=NSEW, padx=10)

        # Icon For URL Button
        icoURL = ImageTk.PhotoImage(Image.open("icon/icon_url.png").resize((30, 30), Image.Resampling.LANCZOS))

        # Get Url Image Button 
        btnUrlImg = Button(self, image=icoURL, text="Liên kết hình ảnh", width=190, height=40, compound="left", command=inputUriBox)
        btnUrlImg.image = icoURL
        btnUrlImg.grid(column=0, row=1, pady=10)

        # Icon For Snip Screen Button
        icoSnipScr = ImageTk.PhotoImage(Image.open("icon/snip_screen.png").resize((30, 30), Image.Resampling.LANCZOS))
        
        # Snip Screen Button
        btnSnipScr = Button(self, image=icoSnipScr, text="Chụp ảnh màn hình", width=190, height=40, compound="left", command=showText)
        btnSnipScr.image = icoSnipScr
        btnSnipScr.grid(column=1, row=1, pady=10)

        # Icon Copy To Clipboard
        icoClipboard = ImageTk.PhotoImage(Image.open("icon/icon_clipboard.png").resize((30, 30), Image.Resampling.LANCZOS))

        # Copy Content To Clipboard
        btnCopy = Button(self, image=icoClipboard, text="Sao chép vào bộ nhớ tạm", width=190, height=40, compound="left", command=showText)
        btnCopy.image = icoClipboard
        btnCopy.grid(column=2, row=1, pady=10)


        # Thiết đặt kích thước cách cột trong khung hinh
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)