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
        #img.flags.writeable = True
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
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
                
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
            self.dupsko=1
            self.Lmlist=[self.nose_y,self.left_shoud_x,self.right_shoud_x,self.left_wrist_y,self.right_wrist_y]
            #dzialajaca lista
            #print(self.Lmlist)
            #self.nos=[int(nose_x),int(nose_y)]
            #print(nos)
        return img


    

  