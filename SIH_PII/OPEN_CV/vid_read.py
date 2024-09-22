import cv2 as cv
capture = cv.VideoCapture(
    r'D:\SIH_PII\OPEN_CV\Video\1536315-hd_1920_1080_30fps.mp4')
while True:
    isTrue, frame = capture.read()  # capturing each frame
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

"""
Traceback (most recent call last):
File "d:\SIH_PII\OPEN_CV\vid_read.py", line 6, in <module>
cv.imshow('video', frame)
cv2.error: OpenCV(4.10.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:973: 
error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow' # VIDEO RAN OUT OF FRAMES AND STOPPED
"""