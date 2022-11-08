import mediapipe as mp
import cv2
import time

mpDraw=mp.solutions.drawing_utils
mpHolistic=mp.solutions.holistic
holistic=mpHolistic.Holistic()

cap=cv2.VideoCapture(0)
ptime=0
while True:
    success,img=cap.read()
    imageRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=holistic.process(imageRGB)
    
    #print(results.face_landmarks)
    if results.pose_landmarks:
       mpDraw.draw_landmarks(img,results.pose_landmarks,mpHolistic.POSE_CONNECTIONS)


    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime


    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
   
    cv2.imshow("Image",img)
    if cv2.waitKey(1)==ord('q'):
      break

cap.release()
cv2.destroyAllWindows
