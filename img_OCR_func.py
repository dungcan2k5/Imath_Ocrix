import os, io
from google.cloud import vision

from snip_screen import *

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = rf"{os.getcwd()}\Key.json"

# Phát hiện văn bản trong tài liệu.
def detect_document():
    snip_screen()

    client = vision.ImageAnnotatorClient()

    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    full_page = response.full_text_annotation.text
    
    return full_page
            
# Phát hiện văn bản trong hình ảnh.
def detect_text():
    snip_screen()

    client = vision.ImageAnnotatorClient()

    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)

    texts = response.text_annotations

    return texts[0].description

# Detect text in image from uri
def detect_text_uri(uri):

    client = vision.ImageAnnotatorClient()

    image = vision.Image()

    image.source.image_uri = uri

    response = client.text_detection(image=image)

    texts = response.text_annotations

    return texts[0].description