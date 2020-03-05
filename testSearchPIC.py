import cv2
import numpy as np

path ='pmq.jpg'
min_w,max_w,min_h,max_h=290,350,150,200
im = cv2.imread(path)
    
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2) 
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt)>30:
       [x,y,w,h] = cv2.boundingRect(cnt)
       if (h>min_h and h<max_h) and (w>min_w and w<max_w):
           cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
           
#cv2.imshow('thresh',thresh)
cv2.imshow('image',im)
         
cv2.waitKey(0)
cv2.destroyAllWindows()

