from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import requests
import pyperclip


from define import *
from img_OCR_func import *
from snip_screen import file_name


class ScrImg(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self["bg"] = COLOR_BACKGROUND
        self.pack(padx = 10, pady = 10)

        # Resize Image
        def resizeImg(option, uri):
            if option == "uri":
                # Get Image
                response = requests.get(uri)
                im = Image.open(BytesIO(response.content))
                height = im.height
                width = im.width

                # Resize Image
                if im.width > 425:
                    height = round(410 * (im.height / im.width))
                    width = 410
                
                return im.resize((width, height), Image.Resampling.LANCZOS)
            elif option == "image":
                # Open image
                im = Image.open(f"Img_temp/{file_name}.png")
                height = im.height
                width = im.width

                # Resize Image
                if im.width > 425:
                    height = round(410 * (im.height / im.width))
                    width = 410

                return im.resize((width, height), Image.Resampling.LANCZOS)

        # Input Uri of Image
        def inputUriBox():

            UrlInputBox = Toplevel()
            content = Entry(UrlInputBox)
            content.pack()
            
            # Show Text of Image
            def click():
                uri = content.get()

                # Detect text from uri
                text = detect_text_uri(uri)
                showTextLabel.config(state="normal")
                showTextLabel.delete('1.0', END)
                showTextLabel.insert("end", text)
                showTextLabel.config(state="disabled")
                
                # Resize Image
                resized = resizeImg("uri", uri)
                imgUri = ImageTk.PhotoImage(resized) 

                # Show Image
                showImgLabel.config(state="normal")
                showImgLabel.delete('1.0', END)
                showImgLabel.image_create(END, image=imgUri)
                showImgLabel.image = imgUri
                showImgLabel.config(state="disabled")

                UrlInputBox.destroy()
                
            Button(UrlInputBox, text="OK", command=click).pack()
        
        # copy selected text to clipboard
        def copyText(): 
            showTextLabel.tag_add("sel", "1.0","end")
            showTextLabel.tag_config("sel",background="black",foreground="white")
            content = showTextLabel.selection_get()
            pyperclip.copy(content)

        # Show text detected from Image
        def showText():
            # Detect text from image
            text = detect_text()
            showTextLabel.config(state="normal")
            showTextLabel.delete('1.0', END)
            showTextLabel.insert("end", text)
            showTextLabel.config(state="disabled")

            # Resize Image
            resized = resizeImg("image", None)
            imgCapScr = ImageTk.PhotoImage(resized)

            # Show Image
            showImgLabel.config(state="normal")
            showImgLabel.delete('1.0', END)
            showImgLabel.image_create(END, image=imgCapScr)
            showImgLabel.image = imgCapScr
            showImgLabel.config(state="disabled")

        # Show Image Label
        showImgLabel = Text(self, bg="light yellow", height=20, font=("Times New Roman", 11))
        showImgLabel.grid(columnspan=2, row=0, padx=10)

        # Show Text Label
        global showTextLabel
        showTextLabel = Text(self, bg="white", height=20, font=("Times New Roman", 11))
        showTextLabel.grid(column=2, row=0, padx=10)

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
        btnCopy = Button(self, image=icoClipboard, text="Sao chép vào bộ nhớ tạm", width=190, height=40, compound="left", command=copyText)
        btnCopy.image = icoClipboard
        btnCopy.grid(column=2, row=1, pady=10)

        # Thiết đặt kích thước cách cột trong khung hinh
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)