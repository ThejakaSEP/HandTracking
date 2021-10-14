import cv2
import mediapipe as mp
import time # to check the frame rate

cap = cv2.VideoCapture(0)

mpHands  = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks) # to Check whether it detects a hand

    #Extracting each hand
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #Get the information of hands. Landmarks information(x&Y coordinates) and ID number
            for id,lm in enumerate(handLms.landmark):
                print(id,'\n',lm)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    cv2.imshow("image",img)
    cv2.waitKey(1)

