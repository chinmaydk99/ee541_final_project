import cv2
import mediapipe as mp
import time
import numpy as np
import math

class handDetector():
    def __init__(self, mode = False, maxHands = 1, detectionCon = 50, trackCon = 50):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands() 
        self.mpDraw = mp.solutions.drawing_utils
        
    def calculate_bounding_box(self, landmarks, image_shape):
        x_min, y_min = image_shape[1], image_shape[0]
        x_max, y_max = 0, 0
        offset=20
        for lm in landmarks.landmark:
            x, y = int(lm.x * image_shape[1]), int(lm.y * image_shape[0])
            x_min = min(x_min, x)
            y_min = min(y_min, y)
            x_max = max(x_max, x)
            y_max = max(y_max, y)

        return x_min-offset, y_min-offset, x_max+offset, y_max+offset
        
    def findHands(self, img, draw=True):
        x_min, y_min, x_max, y_max =0,0,0,0
        imgSize=224
        imgwhite = np.ones((imgSize,imgSize,3),np.uint8)*255
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)  
                    
                x_min, y_min, x_max, y_max = self.calculate_bounding_box(handLms, img.shape)
                h, w = y_max-y_min, x_max-x_min
                imgCrop = img[y_min:y_max, x_min:x_max]
                
                aspectRatio = h/w
                if aspectRatio>1:
                    k=imgSize/h
                    wCal = math.ceil(k*w)
                    if imgCrop.shape[0] > 0 and imgCrop.shape[1] > 0:
                        imgResize = cv2.resize(imgCrop,(wCal,imgSize))
                        wGap = math.ceil((imgSize-wCal)/2)
                        imgwhite[:,wGap:wCal+wGap] = imgResize
                else:
                    k=imgSize/w
                    hCal = math.ceil(k*h)
                    if imgCrop.shape[0] > 0 and imgCrop.shape[1] > 0:
                        imgResize = cv2.resize(imgCrop,(imgSize,hCal))
                        hGap = math.ceil((imgSize-hCal)/2)
                        imgwhite[hGap:hCal+hGap,:] = imgResize
                
                cv2.imshow('Image Cropped', imgwhite)
                if draw:
                    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        return imgwhite, x_min, y_min, x_max, y_max
    
    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 10, (255,0,255), cv2.FILLED)  #Circle each point
                
        return lmList
                
                
def main():
    pTime = 0 
    cTime = 0 
    cap = cv2.VideoCapture(0)
    detector = handDetector()   
    while True:
        success, img = cap.read()
        imgCropped = detector.findHands(img)
        lmList = detector.findPosition(img)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        cv2.imshow('Video', img)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()