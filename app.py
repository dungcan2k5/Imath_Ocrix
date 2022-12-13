from tkinter import *

from define import *

class App():
    def __init__(self, window) -> None:
        
        # Kích thước
        window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # Tiêu đề
        window.title(WINDOW_TITLE)

        # Khoá kích thước
        window.resizable(False, False)

        # Màu nền
        window['bg'] = COLOR_BACKGROUND

        #Icon
        window.iconbitmap(ICON)
        
