import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'img.jpg' 
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_float = np.float32(gray_image)

harris_corners = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04)

harris_corners = cv2.dilate(harris_corners, None)

image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]  # Mark corners in red

plt.title('Harris Corner Detection')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
