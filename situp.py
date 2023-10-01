import cv2
import cvzone
from cvzone.PoseModule import PoseDetector
import numpy as np

def situps():
    cap = cv2.VideoCapture(0)

    detector=PoseDetector() #Used for detecting the pose
    per = 0
    angle = 0
    color = (0,0,255)
    situps = 0
    dir = 0
    while True:
        _,img = cap.read()
        img = detector.findPose(img)
        lmlist,bbox = detector.findPosition(img,False) #landmark list and boundary box
        if lmlist:
            #print(lmlist)
            angle = detector.findAngle(img,24,26,28)
            per = np.interp(angle,(60,165),(100,0))
            bar_value = np.interp(angle, (40, 165), (15, 15 + 300))
            cv2.rectangle(img, (580, int(bar_value)), (580 + 30, 15 + 300), color, cv2.FILLED)
            cv2.rectangle(img,(580,15),(580+30,15+300),(),3)
            cvzone.putTextRect(img,f'{int(per)} %',(575,350),1.2,2,colorT=(),colorR=color,border=3,colorB=())
            if per == 100:
                if dir == 0:
                    situps += 0.5
                    dir = 1
                    color = (0,255,0)
            elif per == 0:
                if dir == 1:
                    situps += 0.5
                    dir = 0
                    color = (0,255,0)
            else:
                color = (0,0,255)
            cvzone.putTextRect(img,f'Situps: {str(int(situps))}',(40,40),2,2,colorT=(255,255,255),colorR=(255,0,0),border=3,colorB=())
        cv2.imshow('Situp Counter',img)
        if cv2.waitKey(1) == ord('q'):
            break