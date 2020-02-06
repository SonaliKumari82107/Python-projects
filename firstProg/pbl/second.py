import pytesseract as tess

import requests
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('test4.png')
text = tess.image_to_string(img)

# pdf = tess.image_to_pdf_or_hocr('text.png', extension='pdf')
# with open('test.pdf', 'w+b') as f:
#     f.write(pdf)

print(text)






#f73533faae88957