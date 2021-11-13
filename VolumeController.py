import math

import HandTrackingModule as htm
import cv2
import numpy as np
import time
import osascript


##############################'
wCam,hCam = 640,480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

# vol = "set volume output volume " + str(-1)
# osascript.osascript(vol)
# result = osascript.osascript('get volume settings')
# print(result)

while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList)!= 0:
        # print(lmList[4],lmList[8])

        x1,y1 = lmList[4][1],lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx,cy = (x1+x2)//2, (y1+y2)//2
        x3, y3 = lmList[12][1], lmList[12][2] # Middle Finger
        # print(x3,y3)

        cv2.circle(img, (x1,y1), 10, (255,0,0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),2)
        cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)
        # print(length)

        vol = np.interp(length,[25,220],[0,100])
        print(round(length), round(vol))
        vol1 = "set volume output volume " + str(vol)
        osascript.osascript(str(vol1))


        if length < 50:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    cv2.waitKey(1)

    cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
    cv2.imshow("Img", img)

