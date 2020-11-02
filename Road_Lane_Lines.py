import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('Files/testvideo2.mp4')

ret, frame = cap.read()

height, width, channels = frame.shape

ROI_Vertices = np.array([(30, height - 20), (width / 2, height / 2 + 175), (width-20, height - 20)], dtype='int32')


def ROI(image, vertices):
    mask = np.zeros_like(image)
    mask_color = (255,) * channels
    cv2.fillPoly(mask, pts=vertices, color=mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


while ret:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 50, 150)
    open = cv2.morphologyEx(canny, cv2.MORPH_OPEN, kernel=(3, 3), iterations=1)
    dilate = cv2.dilate(open, np.ones((3, 3), np.uint8), iterations=1)
    masked_frame = ROI(dilate, [ROI_Vertices])
    cv2.imshow('Masked', masked_frame)
    # cv2.waitKey(0)
    lines = cv2.HoughLinesP(masked_frame, 2, np.pi/180, 20, maxLineGap=40, minLineLength=80)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == ord(' '):
        break

    ret, frame = cap.read()

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
