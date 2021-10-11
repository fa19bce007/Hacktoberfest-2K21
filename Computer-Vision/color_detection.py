#This code will detect blue color objects in live streaming
import cv2

vid=cv2.VideoCapture(0)

while True:
    flag,img=vid.read()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower=(113,40,47)
    higher=(125,255,255)
    mask=cv2.inRange(hsv,lower,higher)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('IMAGE',img)
    cv2.imshow('FINAL',res)
    if cv2.waitKey(1)==27:
        #cv2.imwrite('ABC.jpg',img)
        break


vid.release()
cv2.destroyAllWindows()
