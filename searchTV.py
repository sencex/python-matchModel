import cv2
import numpy as np
#参数设置
videoPath='pmq.mp4'#1280x720
min_w,max_w,min_h,max_h=280,330,150,250#找电视机框的大小

#打开视频文件
cap=cv2.VideoCapture(videoPath)
#打开摄像头
#cap=cv2.VideoCapture(0)

if cap.isOpened:
    flag=True
    while flag:
        flag,frame=cap.read()#读取视频中的每一帧图像
        if flag==False:
            break
        #图像处理
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#彩色图像转换为灰度
        media=cv2.medianBlur(gray,5)#图像中值处理
        thresh = cv2.adaptiveThreshold(media,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,19,2) #自动阀值分割，高斯领域
        #找轮廓
        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        #contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        key=cv2.waitKey(1)
        for cnt in contours:
            if cv2.contourArea(cnt)>80:
                [x,y,w,h] = cv2.boundingRect(cnt)
                if (h>min_h and h<max_h) and (w>min_w and w<max_w):
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
                    #roi = thresh[y:y+h,x:x+w]
                    #roismall = cv2.resize(roi,(30,30))
        
        
        if key==27:
            break            
        cv2.imshow('Find TV',frame)
        #cv2.imshow('gaussian',thresh)
                

cv2.destroyAllWindows()






    


    


