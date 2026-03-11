import cv2

image = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

canny_configs = [
    (50, 150),
    (100, 200),
    (150, 250)
]

for thresholds in canny_configs:
    canny_edge = cv2.Canny(image, thresholds[0], thresholds[1])
    filename = f'canny_{thresholds[0]}_{thresholds[1]}.jpg'
    cv2.imwrite(filename, canny_edge)
    print(f'Saved: {filename}')
