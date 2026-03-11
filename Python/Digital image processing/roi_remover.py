import cv2
import numpy as np

image = cv2.imread('img.jpg')
x, y, w, h = 50, 50, 200, 200
image[y:y+h, x:x+w] = (255, 255, 255)
cv2.imwrite('image_with_removed_roi.jpg', image)
cv2.imshow('Image with ROI Removed', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
