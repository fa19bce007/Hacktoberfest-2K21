#The code will help to detect faces present in image that user provides

import cv2

img=cv2.imread('hero-right.jpeg',1)#enter your own image in which you want to detect faces
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converting color img to gray

facefile=cv2.CascadeClassifier('face.xml')#linking of file with pycharm

faces=facefile.detectMultiScale(gray,1.3,5)#img,scale factor-1.1 to 1.9 but standard value is 1.3,minimum neighbours value upto 9
#scale factor will compress image according to value after 1
#in face detection we draw rectangles here minimum neightbour will form another rectangle after given distance

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,255,255),2)


cv2.imshow('IMG',img)
cv2.imshow('GRAY',gray)
cv2.waitKey(0)
