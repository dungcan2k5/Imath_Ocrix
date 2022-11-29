from tkinter import *
from PIL import Image, ImageTk


from app import App
from define import *
from img_OCR_func import *

window = Tk()
App(window)

def write():
    text_wait.destroy()
    window.withdraw()

    text.configure(state="normal")
    text.delete(1.0, END)
        
    content = detect_document()
    window.deiconify()
    text.insert(1.0, content)
    text.pack(padx=20)
    text.configure(state="disabled")

def open_img(path, x, y):
    return ImageTk.PhotoImage(Image.open(path).resize((x, y), Image.Resampling.LANCZOS))    

text_wait = Text(width=40, height=20, bg="light yellow")
text_wait.pack(side=RIGHT, padx=20)

text = Text()
    
img_snip = open_img("OCR_PRJ/icon/icon_file.png", 30, 30)
btn_snip = Button(image=img_snip, text="Chụp ảnh màn hình", width=180,height=40, font=("Cascadia Code Bold", 12), compound="left", command=write)
btn_snip.pack(padx=10, pady=10, side=BOTTOM)


window.mainloop()