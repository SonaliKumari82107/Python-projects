import numpy as np
import cv2
import io
import requests

img1=cv2.imread("test.PNG")
cv2.imshow("IMG", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# OCR
url_api="https://api.ocr.space/parse/image"
_, compressedimage= cv2.imencode(".jpg", img1, [1,90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api, files={"test.PNG":file_bytes},data={"apikey":"f73533faae88957"} )

print(result)