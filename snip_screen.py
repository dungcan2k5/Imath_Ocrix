import os, keyboard
import time, datetime
from PIL import ImageGrab

file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
img_path = os.path.join("Img_temp", file_name + ".png")

def snip_screen():
    if os.path.isdir("Img_temp"):
        for f in next(os.walk("Img_temp"))[2]:
            os.remove(os.path.join("Img_temp", f))
    else:
        os.mkdir("Img_temp")

    keyboard.press_and_release('windows + shift + s')

    image = image1 = ImageGrab.grabclipboard()

    while image == image1:
        time.sleep(1.5)
        image = ImageGrab.grabclipboard()

    image.save(os.path.join("Img_temp", file_name + ".png"))
