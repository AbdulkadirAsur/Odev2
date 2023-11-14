import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

while True:

    ret, frame = video_capture.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    red_mask = cv2.inRange(hsv, lower_red, upper_red)

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Red Object Detection", cv2.bitwise_and(frame, frame, mask=red_mask))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()