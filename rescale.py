import cv2 as cv;

# Resizing function
def rescaleFrame(frame, scale):
    #Images, Videos and Live Video
    width = int(frame.shape[1] * scale);
    height = int(frame.shape[0] * scale);
    dimensions = (width, height);


    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA);


def changeRes(width, height):
    #Live video
    capture.set(3, width)
    capture.set(4, height)


# Reading image
img = cv.imread('Photos/cat.jpg');
print('Original frame', img.shape);
img_resized = rescaleFrame(img, 0.5);
print('Re-sized image', img_resized.shape);
cv.imshow('Image', img);
cv.imshow('Resize Image', img_resized);


# Reading videos
capture = cv.VideoCapture('Videos/dog.mp4');
while True:
    isTrue, frame = capture.read();
    frame_resized = rescaleFrame(frame, 0.2);

    cv.imshow('Video', frame);
    cv.imshow('Video Resized', frame_resized);

    if cv.waitKey(20) & 0xFF == ord('d'):
        break;

capture.release();
cv.destroyAllWindows();


cv.waitKey(0);