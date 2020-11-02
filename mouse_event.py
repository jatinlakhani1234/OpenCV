import cv2
import numpy as np

img_color = np.zeros((400, 400, 3), np.uint8)
img = cv2.imread('apple.jpg', 1)
points = []

def click_event(event, x, y, flags, param):
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     print(x, y)
    #     string = str(x) + ', ' + str(y)
    #     cv2.putText(img, string, (x,y), cv2.FONT_ITALIC, 1, (0,255,255), 2)
    #     cv2.imshow('image', img)
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(img, (x,y), 2, (0,0,255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255,0,0), 2)
        cv2.imshow('image', img)

    # if event == cv2.EVENT_RBUTTONDOWN:
    #     b = img[y, x, 0]
    #     g = img[y, x, 1]
    #     r = img[y, x, 2]
    #     strBGR = str(b) + ', ' + str(g) + ', '+ str(r)
    #     cv2.putText(img, strBGR, (x, y), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)
    #     cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        img_color[:, :, 0] = b
        img_color[:, :, 1] = g
        img_color[:, :, 2] = r
        cv2.imshow('img_color', img_color)

cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindow()