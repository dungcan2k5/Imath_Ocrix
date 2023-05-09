from PIL import Image
from pix2tex.cli import LatexOCR
from snip_screen import snip_screen, img_path
import os

def predict_formula():
    snip_screen()
    path = os.path.abspath(img_path)
    img = Image.open(path)
    model = LatexOCR()
    formula = model(img)
    return formula