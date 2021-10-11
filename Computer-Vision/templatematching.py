#This code helps to match common templates(portion) from two images
import cv2
import numpy as np

img1=cv2.imread('c2.jpeg',1)#image to be matched with original image
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

face=cv2.imread('c1.jpeg',1) #original image
gray2=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
h,w=gray2.shape


res=cv2.matchTemplate(gray1,gray2,cv2.TM_CCOEFF_NORMED)#third one is constant or keyword

location=np.where(res>0.4)#condition

for i in zip(*location[::-1]):    #zip will join x and y coordinates
    cv2.rectangle(img1,i,((i[0]+w),(i[1]+h)),(0,0,255),1)

cv2.imshow('ORIGINAL',gray1)
cv2.imshow('FACE',gray2)
cv2.imshow('RES',img1)
cv2.waitKey(0)
