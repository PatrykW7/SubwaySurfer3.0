from bodySkeleton import bodyDetector
import cv2
import mediapipe as mp
import time
import pyautogui
import pydirectinput
from pynput.keyboard import Key, Controller



class drawing(bodyDetector):
    

    def drawingLines(self,img,draw=True):   
        #lewa krawedz 
        h,w,c=img.shape
        pt1=(int(w*0.25),int(h*(-0.5)))
        pt2=(int(w*0.25),int(h*5))
        linia_lewa=[pt1,pt2]
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
        #print(self.nose_x)
        #print(self.right_wrist_y)
        #return self.linia_dolna
        #print(bodyDetector.getPosition.right_wrist_x)
        #print(self.right_wrist_x)
    def crossingLines(self,img,lista):

        self.lista=lista
        print(lista[0])
        #dzialajacy print
        #print(self.dupsko)

        

