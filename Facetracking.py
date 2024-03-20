from utils import *
import cv2

fbRange=[[6200,6800,]]

def findFace(img):
    faceCascade=cv2.CascadeClassifier('haarcascade_mcs_eyepair_big.xml')
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.2,8)




    myFaceListC=[] #C fpr Cemter
    myFaceListArea=[]


    for(x,y,w,h) in faces :
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cx = x + w // 2 #divided by 2
        cy = y+ h // 2
        area= w*h
        
        
        
        cv2.circle(img,(cx,cy),5,(0,255,0),cv2.FILLED)
        myFaceListC.append([cx,cy])
        myFaceListArea.append(area)
        
    if len(myFaceListArea)!=0:
        i=myFaceListArea.index(max(myFaceListArea))
        return img,[myFaceListC[i],myFaceListArea[i]]
        
     
    else:
        
        return img,[[0,0],0]
    
def trackFace (me,info,w,pid,pError):
    area=info[1]
    
    if area >fbRange[1]: 
        fb=-20
    elif area<fbRange[0]:
        fb=20

    
cap=cv2.VideoCapture(0)



while True:
    
    _, img = cap.read()
    img, info= findFace(img)
    print("Area",info[1])
    print("Center",info[0])
    
    cv2.imshow('Image', img)
    cv2.waitKey(1)
    
    
    
    