import cv2
import mediapipe as mp
import time # to check the frame rate

class handDetector():
    def __init__(self,mode=False,maxHands = 2,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands  = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands  = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks) # to Check whether it detects a hand

    #Extracting each hand
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #Get the information of hands. Landmarks information(x&Y coordinates) and ID number
            for id,lm in enumerate(handLms.landmark):
                #print(id,'\n',lm)
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                print(id,cx,cy) #Get the pixel location
                # if id==0:
                cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED) #Drawing a Circle on the ID 0 location
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    cv2.imshow("image",img)
    cv2.waitKey(1)


if __name__ == "__main__":
    main()