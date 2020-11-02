import cv2
import datetime

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

while ret:
    text = "Width : "+str(cap.get(3))+"   Height : "+str(cap.get(4))
    dt = str(datetime.datetime.now())
    frame = cv2.putText(frame, text, (10,20), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1, cv2.LINE_AA)
    frame = cv2.putText(frame, dt, (390,20), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1, cv2.LINE_AA)

    cv2.imshow('Video', frame)
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()