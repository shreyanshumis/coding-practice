import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'img.jpg'  
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(binary_image, kernel, iterations=1)
erosion = cv2.erode(binary_image, kernel, iterations=1)
opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel) 
closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel) 
tophat = cv2.morphologyEx(binary_image, cv2.MORPH_TOPHAT, kernel) 

titles = ['Original', 'Dilation', 'Erosion', 'Opening', 'Closing', 'Top Hat']
images = [binary_image, dilation, erosion, opening, closing, tophat]

plt.figure(figsize=(12, 6))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i], cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()
