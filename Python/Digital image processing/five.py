import cv2
image = cv2.imread('fruitBasket.png')
if image is None:
    print("Error: Could not read the image.")
else:
    cv2.imshow('Displayed Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
