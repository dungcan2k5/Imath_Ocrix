import os, keyboard
import time, datetime
from PIL import ImageGrab

# Path Files
file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
img_path = os.path.join("Img_temp", file_name + ".png")

# Chụp màn hình
def snip_screen():
    "Capture a rectangular portion of your screen"

    # Kiểm tra thư mục chứa ảnh tạm thời
    if os.path.isdir("Img_temp"):
        for f in next(os.walk("Img_temp"))[2]:
            os.remove(os.path.join("Img_temp", f))
    else:
        os.mkdir("Img_temp")

    keyboard.press_and_release('windows + shift + s')

    # Sao chép hình ảnh vào bộ nhớ tạm
    image = image1 = ImageGrab.grabclipboard()

    while image == image1:
        time.sleep(1.5)
        image = ImageGrab.grabclipboard()

    image.save(os.path.join("Img_temp", file_name + ".png"))
