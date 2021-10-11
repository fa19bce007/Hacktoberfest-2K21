#Detecting objects in motion in video
import cv2

vid=cv2.VideoCapture('vtest.avi')

flag,frame1=vid.read()
flag,frame2=vid.read()

while True:
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    flag,thresh=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
    cou,hie=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for c in cou:
        (x,y,w,h)=cv2.boundingRect(c)
        if cv2.contourArea(c)>500:#can pass any value
            cv2.rectangle(frame1,(x,y),((x+w),(y+h)),(0,0,255),3)

    cv2.imshow('FRAME',frame1)
    cv2.imshow('DIFF',thresh)
    frame1=frame2
    flag,frame2=vid.read()
    cv2.waitKey(100)
