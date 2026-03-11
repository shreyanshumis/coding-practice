import cv2
import matplotlib.pyplot as plt
import time
import os

image_path = 'brain_mri.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

methods = {
    'Nearest': cv2.INTER_NEAREST,
    'Linear': cv2.INTER_LINEAR,
    'Cubic': cv2.INTER_CUBIC,
    'Area': cv2.INTER_AREA
}

new_size = (128, 128)  # Example resized dimensions
output_folder = 'resized_images'
os.makedirs(output_folder, exist_ok=True)

times = []

for name, method in methods.items():
    start_time = time.time()
    resized_image = cv2.resize(image, new_size, interpolation=method)
    elapsed_time = time.time() - start_time
    
    save_path = os.path.join(output_folder, f'resized_{name}.png')
    cv2.imwrite(save_path, resized_image)
    
    times.append((name, elapsed_time))

methods, exec_times = zip(*times)
plt.bar(methods, exec_times, color=['blue', 'green', 'orange', 'red'])
plt.xlabel('Interpolation Methods')
plt.ylabel('Execution Time (seconds)')
plt.title('Interpolation Methods vs. Execution Time')
plt.show()
