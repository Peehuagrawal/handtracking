import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import numpy as np

cap = cv2.VideoCapture(0)  # Try 1 if 0 doesn't work

wCam, hCam= 640, 480

cap.set(3, wCam)
cap.set(4, hCam)
pTime=0

detector= htm.handDetector()


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#print(f"Audio output: {device.FriendlyName}")
#print(f"- Muted: {bool(volume.GetMute())}")
#print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")

volRange= volume.GetVolumeRange()
volume.SetMasterVolumeLevel(0, None)
minVol=volRange[0]
maxVol=volRange[1]
vol=0
volBar=0

while True:
    success, img = cap.read()
    img= detector.findHands(img)
    lmlist=detector.findPosition(img, draw=False)
    if len(lmlist)!=0:
        #print(lmlist[4],lmlist[8])
        x1, y1= lmlist[4][1], lmlist[4][2]
        x2, y2= lmlist[8][1], lmlist[8][2]
        cx,cy= (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1), 10, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (255,0,255), cv2.FILLED)
        cv2.line(img, (x2,y2), (x1,y1), (255,0,255), 3)
        cv2.circle(img, (cx,cy), 10, (255,0,255), cv2.FILLED)
            
        length=math.hypot(x2-x1,y2-y1)
        #print(length)

        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volume.SetMasterVolumeLevel(vol, None)
        volBar = np.interp(length, [50, 300], [400,150])


        if length<=50:
            cv2.circle(img, (cx,cy), 10, (0,255,0), cv2.FILLED)

        cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
        cv2.rectangle(img,(50,int(volBar)),(85,400),(0,255,0),cv2.FILLED)


    cTime= time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img, str(int(fps)),(40,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    
    cv2.imshow("Image", img)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
