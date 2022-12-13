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
        Label(self, text="Hình ảnh", font=(5), bg=COLOR_BACKGROUND).grid(columnspan=3, row=0, sticky=W,)
        showImgLabel = Text(self, bg="light yellow", height=7)
        showImgLabel.grid(columnspan=3, row=1, sticky=NSEW, pady=(1, 30))
        # Show Equation
        Label(self, text="Công thức được xác định", font=(5), bg=COLOR_BACKGROUND).grid(columnspan=3, row=2, sticky=W)
        showFormulaLabel = Frame(self, bg="white")
        fig = matplotlib.figure.Figure()
        ax = fig.add_subplot(111)

        canvas = FigureCanvasTkAgg(fig, showFormulaLabel)
        canvas.get_tk_widget().pack(side="top", fill="x", expand=True)


        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # showFormulaLabel.bind("<Return>", graph)
        showFormulaLabel.grid(columnspan=3, row=3, sticky=NSEW, pady=(1, 30))

        # Show Latex
        Label(self, text="LaTex", font=(5), bg=COLOR_BACKGROUND).grid(columnspan=3, row=4, sticky=W)
        showLatexLabel = Text(self, bg="white", height=2, font=("Arial", 16))
        showLatexLabel.grid(columnspan=3, row=5, sticky=NSEW, pady=(1, 30))

        # Icon For Snip Screen Button
        icoSnipScr = ImageTk.PhotoImage(Image.open("icon/snip_screen.png").resize((30, 30), Image.Resampling.LANCZOS))
        
        # Snip Screen Button
        btnSnipScr = Button(self, image=icoSnipScr, text="Chụp ảnh màn hình", width=190, height=40, compound="left", command=display_LaTex)
        btnSnipScr.image = icoSnipScr
        btnSnipScr.grid(column=0, row=6, pady=10)

        # Icon Copy To Clipboard
        icoClipboard = ImageTk.PhotoImage(Image.open("icon/icon_clipboard.png").resize((30, 30), Image.Resampling.LANCZOS))

        # Copy Content To Clipboard
        btnCopy = Button(self, image=icoClipboard, text="Sao chép vào bộ nhớ tạm", width=190, height=40, compound="left", command=copyText)
        btnCopy.image = icoClipboard
        btnCopy.grid(column=1, row=6, pady=10)  

        # Icon Copy To Clipboard
        icoWord = ImageTk.PhotoImage(Image.open("icon/icon_word.png").resize((30, 30), Image.Resampling.LANCZOS))        

        # Copy Content To Word
        btnCopy = Button(self, image=icoWord, text="Sao chép vào Word", width=190, height=40, compound="left", command=copyToWord)
        btnCopy.image = icoWord
        btnCopy.grid(column=2, row=6, pady=10)       

        # Thiết đặt kích thước cách cột trong khung hinh
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

