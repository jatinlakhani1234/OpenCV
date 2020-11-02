import numpy as np
import cv2

img = np.zeros([480,480,3], np.uint8)

img = cv2.line(img, (15, 96), (120,340), (0, 0, 255), 4)
img = cv2.arrowedLine(img, (30,45), (83,264), (0,255,0), 3)
img = cv2.circle(img, (200,300), 100, (255,0,255), 3)
img = cv2.rectangle(img, (225,299), (389,476), (255,255,0), 3)
img = cv2.putText(img, "Hello", (50,250), cv2.FONT_ITALIC, 2, (0,255,255), 2)
cv2.imshow('Name', img)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()