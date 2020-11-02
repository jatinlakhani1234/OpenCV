import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Files/vegetables.jpg')

b, g, r = cv2.split(img)

plt.subplot(1, 3, 1), plt.hist(b.ravel(), bins=256, range=[0, 255])
plt.subplot(1, 3, 2), plt.hist(g.ravel(), bins=256, range=[0, 255])
plt.subplot(1, 3, 3), plt.hist(r.ravel(), bins=256, range=[0, 255])
plt.show()

blue_hist = cv2.calcHist([img], [0], None, [256], [0,255])
green_hist = cv2.calcHist([img], [1], None, [256], [0,255])
red_hist = cv2.calcHist([img], [2], None, [256], [0,255])

plt.subplot(1, 3, 1), plt.plot(blue_hist)
plt.subplot(1, 3, 2), plt.plot(green_hist)
plt.subplot(1, 3, 3), plt.plot(red_hist)
plt.show()