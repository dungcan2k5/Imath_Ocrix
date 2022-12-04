from tkinter import *
from PIL import Image, ImageTk

from app import App
from define import *
from img_OCR_func import *
from math_OCR import ScrMath

# Splash Window
splash_root = Tk()
splash_root.geometry("300x200")
splash_label = Label(text="Splash Screen!", font=("Helvetica", 18)).pack(pady=20)

# Show ScrImg window
def run():
    main_window = Toplevel
    ScrImg(main_window)

# Main Window
class ScrImg():
    def __init__(self, window) -> None:
        splash_root.destroy()
        
        # Show Math_OCR Screen
        def openMathScr():
            math_scr = Toplevel
            ScrMath(math_scr)
            window.withdraw()


        window = Tk()
        App(window)

        # Chọn Loại Chương Trình
        choose_ImgOCR = Button(window, text="Image OCR     |", bg=COLOR_BACKGROUND,borderwidth=0, activebackground=COLOR_BACKGROUND)
        choose_ImgOCR.grid(column=0, row=0, sticky=NE, pady=10)

        choose_MathOCR = Button(window, text="   Math OCR", bg=COLOR_BACKGROUND, 
            borderwidth=0, activebackground=COLOR_BACKGROUND, command=openMathScr)
        choose_MathOCR.grid(column=1, row=0, sticky=NW, pady=10)

        Label(window, text="Đây là trang 1").grid(row=1)

        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1) 
    
splash_root.after(3000, run)
mainloop()