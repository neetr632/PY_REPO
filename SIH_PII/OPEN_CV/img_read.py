import cv2 as cv
file_path = r'high_res/pexels-aulsh99-2860705.jpg'
img = cv.imread(file_path)
cv.imshow("wall", img)
cv.waitKey(0)
