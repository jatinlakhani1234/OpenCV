import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Slider')
cv2.createTrackbar('LH', 'Slider', 0, 255, nothing)
cv2.createTrackbar('LS', 'Slider', 0, 255, nothing)
cv2.createTrackbar('LV', 'Slider', 0, 255, nothing)
cv2.createTrackbar('UH', 'Slider', 255, 255, nothing)
cv2.createTrackbar('US', 'Slider', 255, 255, nothing)
cv2.createTrackbar('UV', 'Slider', 255, 255, nothing)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH', 'Slider')
    ls = cv2.getTrackbarPos('LS', 'Slider')
    lv = cv2.getTrackbarPos('LV', 'Slider')
    uh = cv2.getTrackbarPos('UH', 'Slider')
    us = cv2.getTrackbarPos('US', 'Slider')
    uv = cv2.getTrackbarPos('UV', 'Slider')

    l_b = np.array([lh, ls, lv])
    u_b = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', res)

    key = cv2.waitKey(1)
    if key == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()