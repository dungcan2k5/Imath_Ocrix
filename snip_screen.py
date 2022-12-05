import os, keyboard, time, datetime
from PIL import ImageGrab

# Đường dẫn và tên file ảnh
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

    # Chụp màn hình
    keyboard.press_and_release("windows + shift + s")

    # Sao chép hình ảnh vào bộ nhớ tạm
    image = image1 = ImageGrab.grabclipboard()

    while image == image1:
        time.sleep(1.5)
        image = ImageGrab.grabclipboard()

    # Lưu ảnh theo đường dẫn
    image.save(os.path.join("Img_temp", file_name + ".png"))