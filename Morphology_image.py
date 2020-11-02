import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('diff_balls.jpg', 0)
_, mask = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((3, 3), dtype=np.uint8)
erode = cv2.erode(mask, kernel, iterations=1)
dilate = cv2.dilate(mask, kernel, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
gd = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
top = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

title = ['image', 'mask', 'erode', 'dilate', 'opening', 'closing', 'Gradient', 'Top-Hat']
image = [img, mask, erode, dilate, opening, closing, gd, top]
for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(image[i], 'gray')
    plt.title(title[i])

plt.show()