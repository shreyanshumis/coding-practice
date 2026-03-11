import cv2

image = cv2.imread('fruitBasket.png')
if image is None:
    print("Error: Could not open or find the image.")
    exit()

x, y, w, h = 100, 100, 50, 50 
roi = image[y:y+h, x:x+w]
new_x, new_y = x + 100, y + 50
rows, cols, _ = image.shape
if new_y + h > rows or new_x + w > cols:
    h = min(h, rows - new_y)
    w = min(w, cols - new_x)
    roi = roi[:h, :w]
image[new_y:new_y+h, new_x:new_x+w] = roi

cv2.imshow('Image with copied ROI', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output_image.jpg', image)
