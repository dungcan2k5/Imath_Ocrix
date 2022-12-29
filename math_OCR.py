from tkinter import *
from PIL import Image, ImageTk
import pyperclip
import latex2mathml.converter
import matplotlib
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from define import *
from math_OCR_func import predict_formula
from snip_screen import file_name

class ScrMath(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent["bg"] = COLOR_BACKGROUND
        self["bg"] = COLOR_BACKGROUND
        self.pack(padx = 10, pady = 10)

        # Resize Image
        def resizeImg():
            # Open image
            im = Image.open(f"Img_temp/{file_name}.png")
            height = im.height
            width = im.width

            # Resize Image
            if height != 110:
                width = round(110 * (width / height))
                height = 110

            return im.resize((width, height), Image.Resampling.LANCZOS)

        # copy selected text to clipboard
        def copyText(): 
            showLatexLabel.tag_add("sel", "1.0","end")
            showLatexLabel.tag_config("sel",background="black",foreground="white")
            content = showFormulaLabel.selection_get()
            pyperclip.copy(content)

        # Copy Latex to Word(MathML)
        def copyToWord():
            copyText()
            latex_code = pyperclip.paste()
            mathml_code = latex2mathml.converter.convert(latex_code)
            pyperclip.copy(mathml_code)

        # Draw Formula
        def graph(event=None):
            tmptext = text.strip()
            tmptext = "$"+tmptext+"$"

            ax.clear()
            ax.text(0, 0.3, tmptext, fontsize=30)  
            canvas.draw()

        # Show Latex Formula is predicted
        def display_LaTex():
            global text
            text = predict_formula()
            showLatexLabel.config(state="normal")
            showLatexLabel.delete('1.0', END)
            showLatexLabel.insert("end", text)
            showLatexLabel.config(state="disabled")

            # Resize Image
            resized = resizeImg()
            imgCapScr = ImageTk.PhotoImage(resized)

            # Show Image
            showImgLabel.config(state="normal")
            showImgLabel.delete('1.0', END)
            showImgLabel.image_create(END, image=imgCapScr)
            showImgLabel.image = imgCapScr
            showImgLabel.config(state="disabled")

            graph()

        # Show Image
        Label(self, text="Hình ảnh", font=(8), bg=COLOR_BACKGROUND).grid(columnspan=3, row=0, sticky=W,)
        showImgLabel = Text(self, bg="light yellow", height=7)
        showImgLabel.grid(columnspan=3, row=1, sticky=NSEW, pady=(1, 30))

        # Show Equation
        Label(self, text="Công thức được xác định", font=(8), bg=COLOR_BACKGROUND).grid(columnspan=3, row=2, sticky=W)
        showFormulaLabel = Frame(self, bg="white")
        fig = matplotlib.figure.Figure()
        ax = fig.add_subplot(111)

        canvas = FigureCanvasTkAgg(fig, showFormulaLabel)
        canvas.get_tk_widget().pack(side="top", fill="x", expand=True)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        showFormulaLabel.grid(columnspan=3, row=3, sticky=NSEW, pady=(1, 30))

        # Show Latex
        Label(self, text="LaTex", font=(8), bg=COLOR_BACKGROUND).grid(columnspan=3, row=4, sticky=W)
        showLatexLabel = Text(self, bg="white", height=2, font=("Arial", 16))
        showLatexLabel.grid(columnspan=3, row=5, sticky=NSEW, pady=(1, 30))

        # Icon For Snip Screen Button
        btnSnipScr_img = ImageTk.PhotoImage(Image.open("button/btn_snip_screen.png"))
        
        # Snip Screen Button
        btnSnipScr = Button(self, image=btnSnipScr_img, borderwidth=0, bg=COLOR_BACKGROUND, activebackground=COLOR_BACKGROUND, command=display_LaTex)
        btnSnipScr.image = btnSnipScr_img
        btnSnipScr.grid(column=0, row=6, pady=10)

        # Icon Copy To Clipboard
        btnCopyLaTeX_img = ImageTk.PhotoImage(Image.open("button/btn_copy_LaTeX.png"))

        # Copy Content To Clipboard
        btnCopyLaTeX = Button(self, image=btnCopyLaTeX_img, borderwidth=0, bg=COLOR_BACKGROUND, activebackground=COLOR_BACKGROUND, command=copyText)
        btnCopyLaTeX.image = btnCopyLaTeX_img
        btnCopyLaTeX.grid(column=1, row=6, pady=10)  

        # Icon Copy To Clipboard
        btnCopyWord_img = ImageTk.PhotoImage(Image.open("button/btn_copy_Word.png"))        

        # Copy Content To Word
        btnCopyWord = Button(self, image=btnCopyWord_img, borderwidth=0, bg=COLOR_BACKGROUND, activebackground=COLOR_BACKGROUND, command=copyToWord)
        btnCopyWord.image = btnCopyWord_img
        btnCopyWord.grid(column=2, row=6, pady=10)       

        # Thiết đặt kích thước cách cột trong khung hinh
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)