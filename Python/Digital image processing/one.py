# Write a Python OpenCV Code for image restoration of the noisy leena Image using median filter and Gaussian Filter. Show the output images in the concatenated format. Create the resulting image. 

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('noisyLena.png', cv2.IMREAD_GRAYSCALE)

medianFilter = cv2.medianBlur(image, 5)
gaussFilter = cv2.GaussianBlur(image, (5, 5), 0)
concatenated = np.hstack((image, medianFilter, gaussFilter))

cv2.imwrite('restoredLenaComp.png', concatenated)

plt.figure(figsize=(10, 5))
plt.imshow(concatenated, cmap='gray')
plt.title('Original, Median Filtered, Gaussian Filtered')
plt.axis('off')
plt.show()
