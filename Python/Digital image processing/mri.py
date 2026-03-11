import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

output_dirs = ['resized_images', 'histograms', 'thresholded_images']
for folder in output_dirs:
    os.makedirs(folder, exist_ok=True)
image = cv2.imread('mri.jpeg', cv2.IMREAD_GRAYSCALE)
sizes = [(128, 128), (256, 256), (512, 512)]
interpolation_methods = {
    'NEAREST': cv2.INTER_NEAREST,
    'LINEAR': cv2.INTER_LINEAR,
    'CUBIC': cv2.INTER_CUBIC,
    'LANCZOS4': cv2.INTER_LANCZOS4
}
for size in sizes:
    for method_name, method in interpolation_methods.items():
        resized_image = cv2.resize(image, size, interpolation=method)
        resized_filename = f'resized_images/resized_{size[0]}x{size[1]}_{method_name}.jpg'
        cv2.imwrite(resized_filename, resized_image)
        plt.figure()
        plt.title(f'Histogram for {size[0]}x{size[1]} with {method_name} interpolation')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.hist(resized_image.ravel(), bins=256, range=[0, 256])
        histogram_filename = f'histograms/histogram_{size[0]}x{size[1]}_{method_name}.png'
        plt.savefig(histogram_filename)
        plt.close()

        # Calculate the threshold value using Otsu's method
        _, threshold_value = cv2.threshold(resized_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        print(f'Threshold value for {size[0]}x{size[1]} image with {method_name} interpolation: {threshold_value}')

        # Apply the threshold to the resized image
        _, thresholded_image = cv2.threshold(resized_image, threshold_value, 255, cv2.THRESH_BINARY)
        
        # Save the thresholded image to disk
        thresholded_filename = f'thresholded_images/thresholded_{size[0]}x{size[1]}_{method_name}.jpg'
        cv2.imwrite(thresholded_filename, thresholded_image)

        # Display the thresholded image (optional)
        # cv2.imshow(f'Thresholded {size[0]}x{size[1]} {method_name}', thresholded_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

print("Resizing, histogram generation, thresholding, and saving completed successfully!")
