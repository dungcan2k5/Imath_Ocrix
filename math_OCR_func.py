import subprocess
from snip_screen import snip_screen, img_path
import os

def predict_formula():
    snip_screen()
    path = os.path.abspath(img_path)
    a = subprocess.run(f"pix2tex {path}", stdout = subprocess.PIPE)
    formula = (a.stdout.decode("cp932")).replace(f"{path}: ", "")
    return formula
