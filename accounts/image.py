import pytesseract as tess
import pytesseract as Output
from PIL import Image
import cv2 as cv
import re
#line 7 is optional
tess.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
from pyocr.tesseract import image_to_string
text = image_to_string(Image.open(r'C:\Users\Admin\projects\webapp\media\report\images\med1.png'), lang='eng')

img = cv.cv2.imread(r'C:\Users\Admin\projects\webapp\media\report\images\med1.png')
custom_config = r'-c tessedit_char_whitelist=medical --psm 6'
print(tess.pytesseract.image_to_string(img, config=custom_config))
#TESSERACT_CMD = 'tesseract.exe' if os.name == 'nt' else 'tesseract'

#m = Image.open('c:/Users/Admin/projects/webapp/media/report/images/1.png')
#text = pytesseract.image_to_string('m')

