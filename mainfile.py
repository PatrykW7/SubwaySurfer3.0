import cv2
import mediapipe as mp
import time
import pyautogui
import pydirectinput
from pynput.keyboard import Key, Controller
from bodySkeleton import bodyDetector
from drawing import drawing


def main():
    cap=cv2.VideoCapture(0)
    pTime=0
    detector=bodyDetector()
    draw=drawing()
   # cap=detector.make_1080(cap)
    #lmList=detector.getPosition(img)
    
    
    while True:       
        success,img=cap.read()
        img=detector.findBody(img)
        #img.flags.writeable = False
        img=cv2.flip(img,1)
        detector.getPosition(img)
        #print(detector.right_wrist_y)
        draw.drawingLines(img)
        draw.crossingLines(img,detector.Lmlist)
        #draw.getPosition(img)

        #detector.crossingLines(img)
        
        
        #pydirectinput.keyUp('w')wwwwwwwwwwwwwwwwww
        #pydirectinput.keyDown('w')
        
        #lmList=detector.getPosition(img,draw=False)
        #wyswietlenie okreslonego landmarka
        #if len(lmList)!=0:
        #print(lmList[5])
            #rysowanie w okreslony sposob wybranego punktu (np. 14)
            #jak przestaje wykrywac punkt, to sam sie program wylacza
            #cv2.circle(img,(lmList[14][1],lmList[14][2]),15,(0,0,255),cv2.FILLED)
        cTime=time.time() 
        fps=1/(cTime-pTime)
        pTime=cTime
        
       # print(img.shape[0],img.shape[1])q

        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

        cv2.imshow("Image",img)
        cv2.waitKey(1)
        if cv2.waitKey(1)==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows

if __name__ == "__main__":
    main()