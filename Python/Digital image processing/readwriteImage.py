import cv2

img = cv2.imread('noisyLena.png')
cv2.imshow('Displaying the image:', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
