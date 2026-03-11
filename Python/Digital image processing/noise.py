import cv2
import numpy as np
import random

image = cv2.imread('img.jpg')

def salt_and_pepper_noise(img, prob):
    noisy_img = np.copy(img)
    total_pixels = img.size
    num_salt = int(prob * total_pixels)
    num_pepper = int(prob * total_pixels)
    for _ in range(num_salt):
        i = random.randint(0, img.shape[0] - 1)
        j = random.randint(0, img.shape[1] - 1)
        noisy_img[i, j] = 255
    for _ in range(num_pepper):
        i = random.randint(0, img.shape[0] - 1)
        j = random.randint(0, img.shape[1] - 1)
        noisy_img[i, j] = 0
    return noisy_img

def gaussian_noise(img, mean=0, var=50):
    noise = np.random.normal(mean, var ** 0.5, img.shape).astype(np.uint8)
    noisy_img = cv2.add(img, noise)
    return noisy_img

def impulse_noise(img, prob=0.02):
    noisy_img = np.copy(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if random.random() < prob:
                noisy_img[i, j] = random.choice([0, 255])
    return noisy_img

sp_image = salt_and_pepper_noise(image, 0.01)
gaussian_image = gaussian_noise(image)
impulse_image = impulse_noise(image, 0.01)

median_filtered = cv2.medianBlur(image, 5)
mean_filtered = cv2.blur(image, (5, 5))
gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)
laplacian_filter = cv2.convertScaleAbs(cv2.Laplacian(image, cv2.CV_64F))
smooth_filtered = cv2.boxFilter(image, -1, (5, 5))
low_pass_filtered = mean_filtered
kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
high_pass_filtered = cv2.filter2D(image, -1, kernel)

cv2.imshow('Salt and Pepper Noise', sp_image)
cv2.imshow('Gaussian Noise', gaussian_image)
cv2.imshow('Impulse Noise', impulse_image)
cv2.imshow('Median Filter', median_filtered)
cv2.imshow('Mean Filter', mean_filtered)
cv2.imshow('Gaussian Filter', gaussian_filtered)
cv2.imshow('Laplacian Filter', laplacian_filter)
cv2.imshow('Smoothing Filter', smooth_filtered)
cv2.imshow('Low-Pass Filter', low_pass_filtered)
cv2.imshow('High-Pass Filter', high_pass_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
