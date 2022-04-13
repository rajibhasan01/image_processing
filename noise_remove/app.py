import cv2
import numpy as np

img = cv2.imread("test.jpeg")

averaging = cv2.blur(img, (21, 21))
gaussian = cv2.GaussianBlur(img, (3, 3), 0)
median_1 = cv2.medianBlur(img, 3);
median_2 = cv2.medianBlur(median_1, 3);
median_3 = cv2.medianBlur(median_2, 3);
median = cv2.medianBlur(img, 5);
bilateral = cv2.bilateralFilter(median, 9, 350, 350)
gaussian = cv2.GaussianBlur(bilateral, (7, 7), 0)

cv2.imshow("Original image", img)
cv2.imshow("Averaging", averaging)
cv2.imshow("Gaussian", gaussian)
cv2.imshow("Median", median)
cv2.imshow("Bilateral", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows();