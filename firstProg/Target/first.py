import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

r=Image.open('test2.png')
image =pytesseract.image_to_string(r)

print(image)
k=[]
r2=image.split("\n")
for i in r2:
    r3=i.split(" ")
    k.append(r3)

import xlsxwriter
  
workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()

row = 0
 
for x in k :
    column = 0
    for y in x:
        worksheet.write(row, column, y)
        column += 1
    row +=1
      
workbook.close() 