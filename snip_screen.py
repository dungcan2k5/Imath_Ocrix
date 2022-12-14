import os, keyboard, time, datetime, threading
from PIL import ImageGrab

# Đường dẫn và tên file ảnh
file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
img_path = os.path.join("Img_temp", file_name + ".png")

# Chụp màn hình
def snip_screen():
    """Capture a rectangular portion of your screen"""

    # Kiểm tra thư mục chứa ảnh tạm thời
    if os.path.isdir("Img_temp"):
        for f in next(os.walk("Img_temp"))[2]:
            os.remove(os.path.join("Img_temp", f))
    else:
        os.mkdir("Img_temp")

    # Chụp màn hình
    keyboard.press_and_release("windows + down")
    keyboard.press_and_release("shift + windows + s")
    
    def checkAndSave():
        # Sao chép hình ảnh vào bộ nhớ tạm
        image = image1 = ImageGrab.grabclipboard()

        # Sao chép hình ảnh mới vào bộ nhớ tạm
        while image == image1:
            time.sleep(1.5)
            image = ImageGrab.grabclipboard()

        # Lưu ảnh theo đường dẫn
        image.save(os.path.join("Img_temp", file_name + ".png"))
    
    time.sleep(2)
    threading.Thread(target=checkAndSave()).start()