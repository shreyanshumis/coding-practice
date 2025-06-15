import cv2

image = cv2.imread('image.jpg')
x, y, w, h = 50, 50, 200, 200
roi = image[y:y+h, x:x+w]
cv2.imwrite('roi_image.jpg', roi)
cv2.imshow('Region of Interest', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
