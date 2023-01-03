from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import requests, pyperclip, random

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
                if width != 560:
                    height = round(560 * (height / width))
                    width = 560
                
                return im.resize((width, height), Image.Resampling.LANCZOS)
            elif option == "image":
                # Open image
                im = Image.open(f"Img_temp/{file_name}.png")
                height = im.height
                width = im.width

                # Resize Image
                if width != 560:
                    height = round(560 * (height / width))
                    width = 560

                return im.resize((width, height), Image.Resampling.LANCZOS)

        # Input Uri of Image
        def inputUriBox():

            UrlInputBox = Toplevel()
            UrlInputBox.geometry("400x100")
            UrlInputBox.iconbitmap(ICON)
            Label(UrlInputBox, text="Nhập liên kết tới hình ảnh:", pady=10).pack()            
            content = Entry(UrlInputBox,width=100)
            content.pack(padx=10)
            
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
                
            Button(UrlInputBox, text="OK", command=click).pack(pady=10)
        
        # copy selected text to clipboard
        def copyText(): 
            showTextLabel.tag_add("sel", "1.0","end")
            showTextLabel.tag_config("sel",background="black",foreground="white")
            content = showTextLabel.selection_get()
            pyperclip.copy(content)

        # Show text detected from Image
        def showText():
            # Detect text from image
            lst_func = [detect_text, detect_document]
            text = random.choice(lst_func)()
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
        showImgLabel = Text(self, bg="light yellow", width=200, height=26, font=("Times New Roman", 13), state="disabled")
        showImgLabel.grid(columnspan=2, row=0, padx=10, sticky=NSEW)

        # Show Text Label
        global showTextLabel
        showTextLabel = Text(self, bg="white", width=200, height=26, font=("Times New Roman", 13), state="disabled")
        showTextLabel.grid(column=2, row=0, padx=10, sticky=NSEW)

        # Button Image For URL Button
        btnUrlImg_img = ImageTk.PhotoImage(Image.open("button/btn_url.png"))

        # Get Url Of Image Button 
        btnUrlImg = Button(self, image=btnUrlImg_img, borderwidth=0, bg=COLOR_BACKGROUND, activebackground=COLOR_BACKGROUND, cursor="hand2", command=inputUriBox)
        btnUrlImg.image = btnUrlImg_img
        btnUrlImg.grid(column=0, row=1, pady=15)

        # Button Image For Snip Screen Button
        btnSnipScr_img = ImageTk.PhotoImage(Image.open("button/btn_snip_screen.png"))
        
        # Snip Screen Button
        btnSnipScr = Button(self, image=btnSnipScr_img, borderwidth=0, bg=COLOR_BACKGROUND, activebackground=COLOR_BACKGROUND, cursor="hand2", command=showText)
        btnSnipScr.image = btnSnipScr_img
        btnSnipScr.grid(column=1, row=1, pady=15)

        # Button Image Copy To Clipboard
        btnCopy_img = ImageTk.PhotoImage(Image.open("button/btn_copy.png"))

        # Copy Content To Clipboard
        btnCopy = Button(self, image=btnCopy_img, borderwidth=0, bg=COLOR_BACKGROUND, activebackground=COLOR_BACKGROUND, cursor="hand2", command=copyText)
        btnCopy.image = btnCopy_img
        btnCopy.grid(column=2, row=1, pady=15)

        # Thiết đặt độ rộng các cột trong khung hinh
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)