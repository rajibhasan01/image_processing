import cv2 as cv;
import numpy as np;

# numpy.zeros(shape, dtype = None, order = 'C')
blank = np.zeros((500,500,3), dtype='uint8');
cv.imshow('Blank', blank);

# 1. Paint the image a certain colour
# blank[200:300, 300:400] = 0,0,255;
# cv.imshow('Green', blank);


# 2. Draw a Rectangle
# cv2.rectangle(image, start_point, end_point, color, thickness);
cv.rectangle(blank, (0,0),(250,500), (0,255,0), thickness=-1);
cv.imshow('Rectangle', blank);

# 3. Draw a Circle
# cv2.circle(image, center_coordinates, radius, color, thickness)
cv.circle(blank,((blank.shape[0]//2),blank.shape[1]//2), 100, (0,0,255), thickness=-1);
cv.imshow('Circle', blank);

# 4. Draw a Line
# cv2.line(image, start_point, end_point, color, thickness)
cv.line(blank,(0,250),(500,250),(0,255,255), thickness= 2);
cv.imshow('Line', blank);

# 5. Put Text on Image
# cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
cv.putText(blank, 'Rajib Hasan', (150,240), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 1);
cv.imshow('Text', blank);


cv.waitKey(0);