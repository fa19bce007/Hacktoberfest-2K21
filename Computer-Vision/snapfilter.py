#This code is related to applying snap chat filters on image
from PIL import Image
import cv2

bg = Image.open('zayn.jpg')
mask = Image.open('snapchat.png')

img = cv2.imread('zayn.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

facefile = cv2.CascadeClassifier('face.xml')

faces = facefile.detectMultiScale(gray)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,255,255),2)
    mask = mask.resize((w+5, h+5))#used for resizing the image
    bg.paste(mask,(x-5,y+10),mask=mask)

bg.save('newimg.jpg')
newbg=cv2.imread('newimg.jpg')
cv2.imshow('filter',newbg)
cv2.imshow('IMG',img)
cv2.waitKey(0)
