import cv2
import numpy as np

img = cv2.imread('Rubber.jfif')
w, h, c = img.shape
z = np.zeros((w, h), dtype=np.uint8)
blue = np.zeros(img.shape, dtype=np.uint8)
green = np.zeros(img.shape, dtype=np.uint8)
red = np.zeros(img.shape, dtype=np.uint8)

b, g, r = cv2.split(img)

blue[:, :, 0] = b
green[:, :, 1] = g
red[:, :, 2] = r

cv2.imshow('image', img)
cv2.imshow('Blue', blue)
cv2.imshow('Green', green)
cv2.imshow('Red', red)
cv2.imshow('Yellow', cv2.merge((z,g,r)))
cv2.imshow('Magenta', cv2.merge((b,z,r)))
cv2.imshow('Cyan', cv2.merge((b,g,z)))

cv2.waitKey(0)
cv2.destroyAllWindows()