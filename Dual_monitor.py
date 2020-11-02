import cv2

img = cv2.imread('Dual-Monitor-Wallpaper-1.jpg')
print(img.shape)

left = img[:, :1920, :]
right = img[:, 1920:, :]

# cv2.imshow('image', img)
# cv2.imshow('Left', left)
cv2.imshow('Right', right)

cv2.imwrite('Dual_Left.jpg', left)
cv2.imwrite('Dual_Right.jpg', right)

cv2.waitKey(0)
cv2.destroyAllWindows()