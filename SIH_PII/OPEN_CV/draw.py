import cv2 as cv
import numpy as np 
blank = np.zeros((500,500,3), dtype='uint8') 
# The numpy.zeros function creates a new array filled with zeros. In the context of image processing, it is often used to create a blank or black image of a specific size and number of channels

blank_a = np.zeros((500,500,3), dtype='uint8')
# print the image green or a certain colour

blank[200:300, 300:400] = 0,255,0 # you can choose the range to color in the wind0w

# 1. draw a rectangle

cv.rectangle(blank,(50,50),(250,150),(25,125,25), thickness=7) # window to draw on, coordinates, (length, breadth), thickness of the lines=n
cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0)) # perfectly scaled To the 1/4 of the window
# cv.rectangle(), the blank parameter is the image on which the rectangle will be drawn.

# 2. draw a circle

cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 80, (0,0,255), thickness=-1 )

# 3. draw a line

cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0))

# 4. write a text

cv.putText(blank, "hello", (0,175), cv.FONT_HERSHEY_TRIPLEX, 2.0, (0, 255, 0), 2)
cv.imshow('Text', blank )

cv.imshow('rectangle', blank)

cv.waitKey(0)