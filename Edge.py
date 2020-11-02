""" Canny edge detection
5 Steps:
1. Noise Reduction.
2. Gradient Calculation.
3. Non-Maximum Suppression.
4. Double Threshold.
5. Edge tracking by hysteresis.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

img = cv2.imread('Cube.png', 0)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=1)
lap = np.uint8(np.absolute(lap))

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobel_combined = cv2.bitwise_or(sobelx, sobely)

cv2.namedWindow('Slider')
cv2.createTrackbar('LT', 'Slider', 0, 255, nothing)
cv2.createTrackbar('UT', 'Slider', 0, 255, nothing)
while True:
    lt = cv2.getTrackbarPos('LT', 'Slider')
    ut = cv2.getTrackbarPos('UT', 'Slider')
    canny = cv2.Canny(img, lt, ut)
    cv2.imshow('Canny', canny)
    key = cv2.waitKey(1)
    if key == ord(' '):
        break

title = ['image', 'Laplacian', 'sobel-x', 'sobel-y', 'Sobel-Combined', 'Canny']
image = [img, lap, sobelx, sobely, sobel_combined, canny]
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(image[i], 'gray')
    plt.title(title[i])

plt.show()

cv2.destroyAllWindows()