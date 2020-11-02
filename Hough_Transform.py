"""
1. Gray
2. Edge Detection
3. Mapping of points(of edges) in Hough Space and storage in an Accumulator.
4. Interpretation of accumulator to yield lines of infinite length. (Thresholding)
5. Conversion of infinite lines to finite lines.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Files/Cube.png')
image2 = img.copy()
cv2.imshow('Image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 80, 110, apertureSize=3)
lines = cv2.HoughLines(edge, 1, np.pi / 180, 60)
lines2 = cv2.HoughLinesP(edge, 1, np.pi/180, 20, minLineLength=10, maxLineGap=15)
print(lines2)
cv2.imshow('Edges', edge)

for line in lines:
    rho, theta = line[0]
    x0 = rho * np.cos(theta)
    y0 = rho * np.sin(theta)
    x1 = int(x0 + 1000 * (-np.sin(theta)))
    y1 = int(y0 + 1000 * (np.cos(theta)))
    x2 = int(x0 - 1000 * (-np.sin(theta)))
    y2 = int(y0 - 1000 * (np.cos(theta)))
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 1)

cv2.waitKey(0)
cv2.imshow('Image', img)

for line in lines2:
    x1, y1, x2, y2 = line[0]
    cv2.line(image2, (x1, y1), (x2, y2), (255, 255, 0), 2)

cv2.waitKey(0)
cv2.imshow('Image2', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()