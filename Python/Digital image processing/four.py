# Write a code to create 4 parts of the image using ROI and write four different images to the disk. 

import cv2

image = cv2.imread('noisyLena.png')

height, width, _ = image.shape
x1, y1 = 0, 0
x2, y2 = width // 2, height // 2
part1 = image[y1:y2, x1:x2]

x1, y1 = width // 2, 0
x2, y2 = width, height // 2
part2 = image[y1:y2, x1:x2]

x1, y1 = 0, height // 2
x2, y2 = width // 2, height
part3 = image[y1:y2, x1:x2]

x1, y1 = width // 2, height // 2
x2, y2 = width, height
part4 = image[y1:y2, x1:x2]
cv2.imwrite('image_part1.png', part1)
cv2.imwrite('image_part2.png', part2)
cv2.imwrite('image_part3.png', part3)
cv2.imwrite('image_part4.png', part4)
cv2.imshow('Part 1', part1)
cv2.imshow('Part 2', part2)
cv2.imshow('Part 3', part3)
cv2.imshow('Part 4', part4)
cv2.waitKey(0)
cv2.destroyAllWindows()
