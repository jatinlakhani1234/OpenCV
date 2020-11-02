import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Noise_salt_and_pepper.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25

f2d = cv2.filter2D(img, -1, kernel)  # Homogeneous filter. Just takes the of kernel.
blur = cv2.blur(img, (5, 5))  # Averaging.
gblur = cv2.GaussianBlur(img, (5, 5), 0)  # Center has higher weight than neighbours.
median = cv2.medianBlur(img, 5)  # Used for Salt and Pepper noise.
bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75)  # Smoothens the image but keeps the edges sharp.

title = ['image', 'Filter2D', 'blur', 'Gaussian blur', 'Median', 'Bilateral']
image = [img, f2d, blur, gblur, median, bilateral_filter]
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(image[i], 'gray')
    plt.title(title[i])

plt.show()
