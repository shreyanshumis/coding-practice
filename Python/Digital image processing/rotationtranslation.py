import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'input_image.jpg'  
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)
angle = 45
scale = 1.0

rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])
translated_image = cv2.warpAffine(image, translation_matrix, (w, h))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Rotated Image')
plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Translated Image')
plt.imshow(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))

plt.show()
