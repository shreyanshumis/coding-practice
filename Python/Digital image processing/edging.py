import cv2
import numpy as np

image = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

configurations = [
    {"dx": 1, "dy": 0, "ksize": 3},  # Sobel X
    {"dx": 0, "dy": 1, "ksize": 3},  # Sobel Y
    {"dx": 1, "dy": 1, "ksize": 5},  # Combined X and Y
    {"dx": 1, "dy": 1, "ksize": 7}   # Larger kernel
]

for config in configurations:
    sobel_edge = cv2.Sobel(image, cv2.CV_64F, config["dx"], config["dy"], ksize=config["ksize"])
    abs_sobel = cv2.convertScaleAbs(sobel_edge)
    
    filename = f'sobel_dx{config["dx"]}_dy{config["dy"]}_ksize{config["ksize"]}.jpg'
    cv2.imwrite(filename, abs_sobel)
    print(f'Saved: {filename}')
