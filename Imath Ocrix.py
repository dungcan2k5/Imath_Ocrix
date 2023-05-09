from tkinter import *
from PIL import Image, ImageTk
import webbrowser

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

        # Mở liên kết
        def callback(url):
            webbrowser.open_new(url)

        # Cửa sổ giới thiệu:
        def infoWindow():
            info = Toplevel()
            info.geometry("400x210")
            info.iconbitmap(ICON)
            info.title("About Imath Ocrix")
            info.resizable(False, False)

            icoApp = ImageTk.PhotoImage(Image.open("icon/icon_app.png").resize((50, 50), Image.Resampling.LANCZOS))
            heading = Label(info, image=icoApp, text="Imath Ocrix - Phần mềm quét quang học", compound="left")
            heading.image = icoApp
            heading.pack(pady=10)

            Label(info, text="Dự án KHKT 2022-2023 Dũng&Đạt THPT Than Uyên").pack(pady=(10, 0))

            Label(info, text="Mã nguồn của dự án (Github):").pack(pady=(20, 10))
            sourceLink = Label(info, text="https://github.com/dungcan2k5/Imath_Ocrix", fg="blue", cursor="hand2")
            sourceLink.pack()
            sourceLink.bind("<Button-1>", lambda e: callback("https://github.com/dungcan2k5/Imath_Ocrix"))

        # Giới thiệu về chương trình
        icoInfo = ImageTk.PhotoImage(Image.open("icon/icon_info.png").resize((20, 20), Image.Resampling.LANCZOS))
        btnInfo = Button(master, image=icoInfo, borderwidth=0, bg=COLOR_BACKGROUND, activebackground=COLOR_BACKGROUND, command=infoWindow)
        btnInfo.image = icoInfo
        btnInfo.place(x=10, y=10)

        # Điều hướng chọn chương trình
        navigation_frame = Frame(master, borderwidth=0)
        navigation_frame.pack()

        # Chọn chương trình con ImgOCR
        global choose_ImgOCR
        choose_ImgOCR = Button(navigation_frame, text="Image OCR", font=("Segoe UI Semibold", 12, 'underline'), padx=10, pady=10, bg=COLOR_BACKGROUND, activebackground=COLOR_BACKGROUND,  borderwidth=0, cursor="hand2", command=self.switchScrImg)
        choose_ImgOCR.grid(column=0, row=0, sticky=NE)

        # Chọn chương trình con ImgMath
        global choose_MathOCR
        choose_MathOCR = Button(navigation_frame, text="Math OCR", font=("Segoe UI Semibold", 12, 'underline'), padx=10, pady=10, bg=COLOR_BACKGROUND, borderwidth=0, activebackground=COLOR_BACKGROUND, cursor="hand2", command=self.switchScrMath)
        choose_MathOCR.grid(column=1, row=0, sticky=NW)
        choose_MathOCR.configure(font=("Segoe UI", 12))
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
        choose_ImgOCR.configure(font=("Segoe UI Semibold", 12, 'underline'))
        choose_MathOCR.configure(font=("Segoe UI", 12))
        self.framelist[1].forget()
        self.framelist[0].tkraise()
        self.framelist[0].pack(padx = 10, pady = 10)

    def switchScrMath(self):
        """Chuyển sang khung MathImg"""
        choose_MathOCR.configure(font=("Segoe UI Semibold", 12, 'underline'))
        choose_ImgOCR.configure(font=("Segoe UI", 12))
        self.framelist[0].forget()
        self.framelist[1].tkraise()
        self.framelist[1].pack(padx = 10, pady = (20, 10))

# Màn hình giới thiệu
splash_root = Tk()
splash_root.geometry("300x150")
splash_root.overrideredirect(True)
splash_img = ImageTk.PhotoImage(Image.open("icon/Splash Screen.png"))
splash_label = Label(image=splash_img).pack()
# splash_label.image = splash_img

# Hiển thị màn hình chính
def run():
    main_window = Toplevel
    MainWindow(main_window)
splash_root.after(1, run)
mainloop()