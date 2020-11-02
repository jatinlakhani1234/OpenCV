"""
At each increasing level, there is a repeated smoothing and subsampling.
A level in Laplacian Pyramid is formed by the diff btwn that level in Gaussian pyramid and the expanded version of
its upper level in Gaussian Pyramid.
"""

import cv2

img = cv2.imread('images.jpg')
print(img.shape)
img = cv2.resize(img, (256, 208))
layer = img.copy()
cv2.imshow('Image', img)
gp = [layer]
lp = []
for i in range(3):
    down = cv2.pyrDown(layer)
    up = cv2.pyrUp(down)
    lap_lyr = cv2.subtract(layer, up)
    lp.append(lap_lyr)
    layer = down
    gp.append(layer)
    cv2.imshow('Gauss'+str(i+1), layer)
    cv2.imshow('Lap'+str(i+1), lap_lyr)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()