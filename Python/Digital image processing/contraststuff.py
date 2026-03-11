import cv2
import numpy as np
image = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

# Contrast stretching
min_pixel = np.min(image)
max_pixel = np.max(image)
stretched_image = ((image - min_pixel) / (max_pixel - min_pixel) * 255).astype(np.uint8)

cv2.imshow('Original Image', image)
cv2.imshow('Contrast Stretched Image', stretched_image)
cv2.imwrite('contrast_stretched_image.jpg', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
