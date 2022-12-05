from tkinter import *

from app import App
from define import *

from img_OCR import ScrImg
from math_OCR import ScrMath
 
class MainWindow():
    def __init__(self, master):
        splash_root.destroy()

        master = Tk()
        App(master)

        # Điều hướng chọn chương trình
        navigation_frame = Frame(master, borderwidth=0)
        navigation_frame.pack()

        # Chọn chương trình ImgOCR
        choose_ImgOCR = Button(navigation_frame, text="Image OCR     |", pady=10, bg=COLOR_BACKGROUND, borderwidth=0, activebackground=COLOR_BACKGROUND, command=self.switchScrImg)
        choose_ImgOCR.grid(column=0, row=0, sticky=NE)

        # Chọn chương trình ImgMath
        choose_MathOCR = Button(navigation_frame, text="   Math OCR", pady=10, bg=COLOR_BACKGROUND, borderwidth=0, activebackground=COLOR_BACKGROUND, command=self.switchScrMath)
        choose_MathOCR.grid(column=1, row=0, sticky=NW)


        mainframe = Frame(master)
        mainframe.pack(padx=10, pady=10, fill='both', expand=1)
        self.windowNum = 0
 
        self.framelist = []
        self.framelist.append(ScrImg(mainframe))
        self.framelist.append(ScrMath(mainframe))
        self.framelist[1].forget()
 
    def switchScrImg(self):
        self.framelist[1].forget()
        self.framelist[0].tkraise()
        self.framelist[0].pack(padx = 10, pady = 10)

    def switchScrMath(self):
        self.framelist[0].forget()
        self.framelist[1].tkraise()
        self.framelist[1].pack(padx = 10, pady = 10)
 
# Splash Window
splash_root = Tk()
splash_root.geometry("300x200")
splash_label = Label(text="Splash Screen!", font=("Helvetica", 18)).pack(pady=20)

# Show Main Window
def run():
    main_window = Toplevel
    MainWindow(main_window)

splash_root.after(3000, run)
mainloop()