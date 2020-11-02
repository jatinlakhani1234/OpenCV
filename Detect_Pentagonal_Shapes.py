"""
1. Gray
2. Binary
3. Contour
"""
import cv2
import numpy as np

img = cv2.imread('Files/polygons_labeled.jpg')
kernel = np.ones((3, 3), np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
dilate = cv2.dilate(binary, kernel, iterations=3)
# open = cv2.morphologyEx(dilate, cv2.MORPH_OPEN, kernel, iterations=4)

cv2.imshow('Open', dilate)
contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    print(approx.ravel())
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
    x, y = approx.ravel()[:2]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)
    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    elif len(approx) == 7:
        cv2.putText(img, "Heptagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    elif len(approx) == 8:
        cv2.putText(img, "Octagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    elif len(approx) == 9:
        cv2.putText(img, "Nonagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    elif len(approx) == 10:
        cv2.putText(img, "Decagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()