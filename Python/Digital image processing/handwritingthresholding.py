import cv2

image = cv2.imread('shreyanshu_notes.jpg', cv2.IMREAD_GRAYSCALE)

_, thresholded_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite('thresholded_handwritten.jpg', thresholded_image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
