import cv2;
import face_recognition;

img = cv2.imread("self/2.jpg");
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);
img_encoding = face_recognition.face_encodings(rgb_img)[0];


img2 = cv2.imread("test/rajib_4.jpg");
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB);
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0];
result = face_recognition.compare_faces([img_encoding], img_encoding2);




print("Result: ", result[0]);

# cv2.imshow('First Image', img);
# cv2.imshow('Second Image', img2);
cv2.waitKey(0)