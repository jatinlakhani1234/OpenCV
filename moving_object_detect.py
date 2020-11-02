"""
1. Difference between 2 frames.
2. Convert to Gray.
3. Gaussian blur.
4. Binary.
5. Dilate.
6. Contour
7. Contour:
    - area threshold
    - Bounding area of Contour
    - Draw a rectangle.
"""

import cv2

cap = cv2.VideoCapture('Files/stock-footage-hong-kong-nov-city-life-in-real-time.webm')
# cap = cv2.VideoCapture('Files/stock-footage-moscow-russia-december-ice-skating-at-the-rink-before-christmas-in-the-mall-vegas-in.webm')
# cap = cv2.VideoCapture('Files/stock-footage-moscow-jan-lot-of-people-skate-on-large-indoor-ice-rink-in-european-europeisky-shopping.webm')
_, frame1 = cap.read()
_, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(binary, None, iterations=3)
    contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 550:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Diff', frame1)

    frame1 = frame2
    _, frame2 = cap.read()

    if cv2.waitKey(1) == ord(' '):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
