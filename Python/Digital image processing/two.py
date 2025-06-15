# Write a Python OpenCV Code Plot the histogram / Distribution plot for an image to see the B, G and R channels separately. Store the histogram plot in PDF file with good resolution, using Python Code. 

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('noisyLena.png')

channels = cv2.split(image)
colors = ('b', 'g', 'r')
channel_names = ('Blue', 'Green', 'Red')

plt.figure(figsize=(10, 6))
for (channel, color, name) in zip(channels, colors, channel_names):
    histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(histogram, color=color, label=f'{name} channel')
    plt.xlim([0, 256])

plt.title('Histogram for B, G, R channels')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('histogram_plot.pdf', dpi=300, format='pdf')
plt.show()
