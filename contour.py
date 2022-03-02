import os;
import cv2 as cv;
import numpy as np;
import pandas as pd;


img = cv.imread('Photos/3.JPEG');


# imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(imgray, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE);
# cv.drawContours(img, contours, -1, (0,255,0), 3);


lower = np.array([0,0,0]);
higher = np.array([255,255,100]);

mask = cv.inRange(img, lower, higher);


cv.imshow('New Img', mask);

cont, _ = cv.findContours(mask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE);
cont_img = cv.drawContours(img, cont, -1, 255,3);

c = max(cont, key = cv.contourArea);

x,y,w,h = cv.boundingRect(c);

cv.rectangle(img, (x,y), (x+w, y+h), (0,255, 0), 5)

cv.imshow('cont_img', cont_img);

  
# The kernel to be used for dilation purpose
# kernel = np.ones((5, 5), np.uint8)
  
# # converting the image to HSV format
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  
# # defining the lower and upper values of HSV,
# # this will detect yellow colour
# Lower_hsv = np.array([0, 0, 0])
# Upper_hsv = np.array([200, 200, 200])
  
# # creating the mask by eroding,morphing,
# # dilating process
# Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
# Mask = cv2.erode(Mask, kernel, iterations=1)
# Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
# Mask = cv2.dilate(Mask, kernel, iterations=1)
  
# # Inverting the mask by
# # performing bitwise-not operation
# Mask = cv2.bitwise_not(Mask);
  
# Displaying the image
cv.imshow('Mask', mask);

cv.imshow('img', img);

cv.waitKey(0);