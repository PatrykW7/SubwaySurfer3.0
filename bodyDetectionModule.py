import mediapipe as mp
import cv2
import time


class bodyDetection():
    def __init__(self,model_complexity=1):
        self.model_complexity=1

        self.mpDraw=mp.solutions.drawing_utils
        self.mpHolistic=mp.solutions.holistic
        self.holistic=self.mpHolistic.Holistic(self.model_complexity)



    def findBody(self,img,draw=True):
        imageRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.holistic.process(imageRGB)
        if self.results.pose_landmarks:
            if draw:
                #kolorowanie - nie konieczne 
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpHolistic.POSE_CONNECTIONS,self.mpDraw.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2))
                

        return img

    def make_1080(self,cap):
        cap.set(3,1920)
        cap.set(4,1080)
        return cap

    def change_res(self,cap,width,height):
        cap.set(3,width)
        cap.set(4,height)

    def rescale_frame(self,img,percent=75):
        scale_percent=75
        width=int(img.shape[1]*scale_percent/100)
        height=int(img.shape[0]*scale_percent/100)
        dim=(width/height)
        return cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

    def getPosition(self,img):
        lmList=[]
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
        return lmList
                
def main():
    
    cap=cv2.VideoCapture(0)
    detector=bodyDetection()
    cap=detector.make_1080(cap) 
    while True:
        success,img=cap.read()   
           
        img=detector.findBody(img)
        lmList=detector.getPosition(img)
        print(lmList)
        #print(img.shape)
        
        #img=detector.rescale_frame(img)
        #print(img.shape)
        cv2.imshow("Image",img)
        if cv2.waitKey(1)==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows


if __name__=="__main__":
    main()
    