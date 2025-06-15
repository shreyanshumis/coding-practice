import cv2
import numpy as np

image = cv2.imread('img.jpg')

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

angle = 45
scale = 1.0

rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
cv2.imwrite('rotated_image.jpg', rotated_image)

tx, ty = 100, 100
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, translation_matrix, (w + tx, h + ty))
cv2.imwrite('translated_image.jpg', translated_image)
