import cv2
import matplotlib.pyplot as plt

# Load a color image
image = cv2.imread('path_to_image.jpg')

# Convert the color image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Plot the grayscale image
plt.figure(figsize=(6, 6))
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()

# Plot the histogram of the grayscale image
plt.figure(figsize=(6, 4))
plt.hist(gray_image.ravel(), bins=256, range=[0, 256], color='black')
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
