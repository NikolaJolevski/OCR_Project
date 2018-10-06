import cv2
import numpy as np
import pytesseract
import os
from PIL import Image
import re

# Path of working folder on Disk
src_path = "C:/Users/user/Documents/GitHub/OCR_Project/djangoProject/posts/static/"

def get_string(name, lang):
    img_path = src_path + name;
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
   # img = cv2.fastNlMeansDenoising(img)
    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
   # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"), lang=lang)

    # Remove the temporary images
    os.remove(src_path + "thres.png")
    os.remove(src_path + "removed_noise.png")

    # remove the empty lines
    filtered = "".join([s for s in result.splitlines(True) if s.strip("\r\n")])
    # remove multi
    filtered2 = re.sub(' +',' ',filtered)
    return filtered2


print '--- Start recognize text from image ---'
