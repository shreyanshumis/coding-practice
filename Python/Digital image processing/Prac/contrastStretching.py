import cv2
import numpy as np
img = cv2.imread('shreyanshu_notes.jpg')

minpix = np.min(img)
maxpix = np.max(img)
imgStretched = ((img - minpix) / (maxpix - minpix) * 400).astype(np.uint8)

cv2.imwrite('cstretched.jpg', imgStretched)
cv2.imshow('Original img', img)
cv2.imshow('Contrast Stretched for my notes', imgStretched)
cv2.waitKey(0)
