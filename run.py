from tkinter import *

from app import App
from define import *
from img_OCR import ScrImg
from math_OCR import ScrMath
 
class MainWindow():
    def __init__(self, master):
        # Tắt màn hình giới thiệu sau khi vào chương trình
        splash_root.destroy()

        master = Tk()
        App(master)

        # Điều hướng chọn chương trình
        navigation_frame = Frame(master, borderwidth=0)
        navigation_frame.pack()

        # Chọn chương trình con ImgOCR
        choose_ImgOCR = Button(navigation_frame, text="Image OCR     |", pady=10, bg=COLOR_BACKGROUND, borderwidth=0, activebackground=COLOR_BACKGROUND, command=self.switchScrImg)
        choose_ImgOCR.grid(column=0, row=0, sticky=NE)

        # Chọn chương trình con ImgMath
        choose_MathOCR = Button(navigation_frame, text="   Math OCR", pady=10, bg=COLOR_BACKGROUND, borderwidth=0, activebackground=COLOR_BACKGROUND, command=self.switchScrMath)
        choose_MathOCR.grid(column=1, row=0, sticky=NW)

        # Thiết lập khung phần mềm
        mainframe = Frame(master)
        mainframe.pack(padx=10, pady=10, fill='both', expand=1)

        # Thêm ScrImg và ScrMath vào danh sách khung
        self.framelist = []
        self.framelist.append(ScrImg(mainframe))
        self.framelist.append(ScrMath(mainframe))
        self.framelist[1].forget()
 
    def switchScrImg(self):
        """Chuyển sang khung ScrImg"""
        self.framelist[1].forget()
        self.framelist[0].tkraise()
        self.framelist[0].pack(padx = 10, pady = 10)

    def switchScrMath(self):
        """Chuyển sang khung MathImg"""
        self.framelist[0].forget()
        self.framelist[1].tkraise()
        self.framelist[1].pack(padx = 10, pady = 10)

# Màn hình giới thiệu
splash_root = Tk()
splash_root.geometry("300x200")
splash_label = Label(text="Splash Screen!", font=("Helvetica", 18)).pack(pady=20)

# Hiển thị màn hình chính
def run():
    main_window = Toplevel
    MainWindow(main_window)
splash_root.after(1, run)
mainloop()