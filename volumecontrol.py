import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)  # Try 1 if 0 doesn't work


while True:
    success, img = cap.read()
    
    cv2.imshow("Image", img)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
