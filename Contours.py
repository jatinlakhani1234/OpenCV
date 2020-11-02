import cv2
import numpy as np

kernel = np.ones((3, 3), dtype=np.uint8)
img = cv2.imread('golf_balls.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 95, 255, 0)
open = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)
# close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel)

contour, hierarchy = cv2.findContours(open, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('Number of Contours = ', len(contour))

cv2.drawContours(img, contour, -1, (0, 0, 255), 2)

cv2.imshow('Image', img)
cv2.imshow('Gray', gray)
cv2.imshow('Binary', binary)
cv2.imshow('Open', open)
# cv2.imshow('Close', close)
cv2.waitKey(0)
cv2.destroyAllWindows()