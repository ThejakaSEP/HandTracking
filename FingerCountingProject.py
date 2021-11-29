import cv2
import mediapipe
import time
import os
import HandTrackingModule as htm

wCam,hCam = 640,480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

detector = htm.handDetector(detectionCon=0.75)

tipsIDs = [4,8,12,16,20]

while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers =[]

        #Thumb
        if lmList[tipsIDs[0]][1] > lmList[tipsIDs[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        #4 Fingers
        for id in range(1,5):
            if lmList[tipsIDs[id]][2] < lmList[tipsIDs[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)
        print(fingers)

        cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
        cv2.putText(img,str(totalFingers),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)

    cv2.imshow("Image",img)
    cv2.waitKey(1)

