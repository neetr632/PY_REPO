import cv2 as cv
img = cv.imread('high_res/pexels-aulsh99-2860705.jpg')
cv.imshow('water', img)
def ChangeRes(width, height):
    # Works for live video
    capture.set(3,width)
    capture.set(4,height)
def Rescaleframe(frame, scale=0.25):
    # Works for live video, image , video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = Rescaleframe(img)
cv.imshow('image', resized_image)

capture = cv.VideoCapture('Video/2311965-hd_1280_720_50fps.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = Rescaleframe(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()