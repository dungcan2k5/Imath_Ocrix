from tkinter import *

from define import *

class App():
    def __init__(self, window) -> None:
        
        # Kích thước
        window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_POSITTION_RIGHT}+{WINDOW_POSITTION_DOWN}")

        # Tiêu đề
        window.title(WINDOW_TITLE)

        # Khoá kích thước
        window.resizable(False, False)

        # Màu nền
        window['bg'] = COLOR_BACKGROUND

        # Tên dự án
        Label(text="Máy Quét Quang Học", bg=COLOR_BACKGROUND, font=("Cascadia Mono Bold", 20)).pack(pady=10)

        