import cv2
import numpy as np

img = cv2.imread('img.png')
x, y, w, h = 50, 50, 200, 200
img[y:y+h, x:x+w] = (255, 255, 255)
cv2.imwrite('roiRemoved.jpg', img)
cv2.imshow('ROI removed from Amity syllabus', img)
cv2.waitKey(0)
