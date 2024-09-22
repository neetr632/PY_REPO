import cv2 as cv
import numpy as np

file_path = r'high_res/pexels-aulsh99-2860705.jpg'
arr = cv.imread(file_path)
row , col = 100, 150
pixel_arr = arr[row, col]
print(f"Pixel value at ({row}, {col}): {pixel_arr}")