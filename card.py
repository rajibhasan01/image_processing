import cv2 as cv;
import pytesseract;
import numpy as np;

image = cv.imread('drive/5.jpg');


width = 1245;
height = 783;
dim = (width, height);


# resize image
resized = cv.resize(image, dim, interpolation = cv.INTER_AREA);
text = pytesseract.image_to_string(resized, lang = 'eng');


print('Details: ', text);
cv.waitKey(0);