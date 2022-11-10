import cv2
import mediapipe as mp
import time
import pyautogui
import pydirectinput
from pynput.keyboard import Key, Controller


class bodyDetector():
    def __init__(self,mode=False,model_complexity=1,smooth=True,ensegm=True,smoth_segm=True,detectionCon=0.5,trackCon=0.5):
       
        self.mode=mode
        self.model_complexity=model_complexity   
        self.smooth=smooth
        self.ensegm=ensegm
        self.smoth_segm=smoth_segm
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpDraw=mp.solutions.drawing_utils
        self.mpPose=mp.solutions.pose       
        self.pose=self.mpPose.Pose(self.mode,self.model_complexity,self.smooth,self.ensegm,self.smoth_segm,self.detectionCon,self.trackCon)
        
        


    def findBody(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #
        #print(dir(self))
        h,w,c=img.shape
        self.results = self.pose.process(imgRGB)    
        if self.results.pose_landmarks:
            left_wrist_x=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.LEFT_WRIST].x*w
            left_wrist_y=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.LEFT_WRIST].y*h
            #wypisywanie wspolrzednych nosa 
            #print(self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.NOSE].x * 360)
            if draw:
                #self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
                
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS,self.mpDraw.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2))
                cv2.circle(img,(int(left_wrist_x),int(left_wrist_y)),15,(255,0,255),cv2.FILLED)
        return img

    def getPosition(self,img,draw=True):

        h,w,c=img.shape
        if self.results.pose_landmarks:
            self.Lmlist=[]
            self.nose_x=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.NOSE].x * w
            self.nose_y=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.NOSE].y * h
            self.left_shoud_x=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.LEFT_SHOULDER].x*w
            self.left_shoud_y=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.LEFT_SHOULDER].y*h
            self.right_shoud_x=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.RIGHT_SHOULDER].x*w
            self.right_shoud_y=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.RIGHT_SHOULDER].y*h
            self.left_wrist_x=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.LEFT_WRIST].x*w
            self.left_wrist_y=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.LEFT_WRIST].y*h
            self.right_wrist_x=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.RIGHT_WRIST].x*w
            self.right_wrist_y=self.results.pose_landmarks.landmark[self.mpPose.PoseLandmark.RIGHT_WRIST].y*h
            #self.nos=[int(nose_x),int(nose_y)]
            nos=(self.nose_x,self.nose_y)
            self.Lmlist.append(nos)
            #print(nos)
        return img, self.Lmlist
    '''
    def make_1080(self,cap):
        cap.set(3,1920)
        cap.set(4,1080)
        return cap
    '''
    def drawingLines(self,img,draw=True):   
        #lewa krawedz 
        h,w,c=img.shape
        pt1=(int(w*0.25),int(h*(-0.5)))
        pt2=(int(w*0.25),int(h*5))
        linia_lewa=[pt1,pt2]
        h,w,c=img.shape
        cv2.line(img,linia_lewa[0],linia_lewa[1],(255,0,255),3)
        #prawa krawedz
        pt1=(int(w*0.75),int(h*(-0.5)))
        pt2=(int(w*0.75),int(h*5))
        linia_prawa=[pt1,pt2]
        cv2.line(img,linia_prawa[0],linia_prawa[1],(255,0,0),3)
        #gorna krawedz
        pt1=(int(w*(-0.5)),int(h*0.2))
        pt2=(int(w*5),int(h*0.2))
        linia_gorna=[pt1,pt2]
        #print(linia_gorna)
        cv2.line(img,linia_gorna[0],linia_gorna[1],(255,0,0),3)
        #dolna krawedz
        pt11=(int(w*(-0.5)),int(h*0.75))
        pt22=(int(w*5),int(h*0.75))
        self.linia_dolna=[pt11,pt22]
        cv2.line(img,self.linia_dolna[0],self.linia_dolna[1],(255,0,0),3)
        #print(self.linia_dolna[0])
        return self.linia_dolna
    def crossingLines(self,img):
        #wypisanie wspolrzednej x linii dolnej
        #print(self.linia_dolna[0])
        #return self.linia_dolna
       # print(self.nos[0])
        print(self.right_shoud_x)
        #if self.Lmlist[1]>=


def main():
    cap=cv2.VideoCapture(0)
    pTime=0
    detector=bodyDetector()
   # cap=detector.make_1080(cap)
    #lmList=detector.getPosition(img)
    
    
    while True:
        success,img=cap.read()
        img=detector.findBody(img)
        img=cv2.flip(img,1)
        detector.drawingLines(img)
        detector.getPosition(img)
        detector.crossingLines(img)
        
        
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