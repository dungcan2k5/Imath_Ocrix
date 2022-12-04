from tkinter import *
from app import App
from define import *
 
class ScrImg(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text = "This is Window 1").pack(padx = 10, pady = 10)
        self.pack(padx = 10, pady = 10)
 
class ScrMath(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text = "This is Window 2").pack(padx = 10, pady = 10)
        self.pack(padx = 10, pady = 10)
 
class MainWindow():
    def __init__(self, master):
        splash_root.destroy()

        master = Tk()
        App(master)

        navigation_frame = Frame(master, borderwidth=0)
        navigation_frame.pack()

        choose_ImgOCR = Button(navigation_frame, text="Image OCR     |", pady=10, bg=COLOR_BACKGROUND, borderwidth=0, activebackground=COLOR_BACKGROUND, command=self.switchScrImg)
        choose_ImgOCR.grid(column=0, row=0, sticky=NE)

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
        
    def switchWindows(self):
        self.framelist[self.windowNum].forget()
        self.framelist[self.windowNum].tkraise()
        self.framelist[self.windowNum].pack(padx = 10, pady = 10)
 
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