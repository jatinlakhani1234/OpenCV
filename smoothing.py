import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Rubber.jfif', 0)

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
_, th6 = cv2.threshold(img, 127, 255, cv2.THRESH_TRIANGLE)

th7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th8 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# cv2.imshow('img', img)
# cv2.imshow('th1', th1)
# cv2.imshow('th2', th2)
# cv2.imshow('th3', th3)
# cv2.imshow('th4', th4)
# cv2.imshow('th5', th5)
# cv2.imshow('th6', th6)
# cv2.imshow('th7', th7)
# cv2.imshow('th8', th8)

title = ['image', 'THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV',
         'THRESH_TRIANGLE', 'ADAPTIVE_THRESH_MEAN_C', 'ADAPTIVE_THRESH_GAUSSIAN_C']
image = [img, th1, th2, th3, th4, th5, th6, th7, th8]
for i in range(9):
    plt.subplot(3,3,i+1), plt.imshow(image[i], 'gray')
    plt.title(title[i])

plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()