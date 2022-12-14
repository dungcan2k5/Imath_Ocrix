import subprocess, pyperclip
from snip_screen import snip_screen, img_path
import os

def predict_formula():
    snip_screen()
    path = os.path.abspath(img_path)
    subprocess.run(f"pix2tex {path}", stdout = subprocess.PIPE)
    formula = pyperclip.paste()
    return formula