# import cv2
# import numpy as np


# # Set up the video capture
# capture = cv2.VideoCapture("second_stage/1_task/videos/7c7ebfc8-f0b0-414f-8a96-99b16e33e937.mp4")

# # Set up the background subtractor
# bgSubtractor = cv2.createBackgroundSubtractorKNN()


# Python code for Background subtraction using OpenCV 
import numpy as np 
import cv2 
  
cap = cv2.VideoCapture("C:/Users/max30/Desktop/videos/061bdfbf-a52b-4788-aa68-91136905e71d.mp4") 
fgbg = cv2.createBackgroundSubtractorMOG2() 
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4)) 
  
while True: 
    ret, frame = cap.read() 
    if not ret:
        break
  
    fgmask = fgbg.apply(frame, learningRate=0.3) 
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)  

    
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(fgmask,contours, -1, (255,0,255), 2)
    for cnt in contours:
        if cv2.contourArea(cnt) > 1000:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
    cv2.imshow('fgmask', frame) 
    #cv2.imshow('frame',frame ) 
  
      
    k = cv2.waitKey(300) & 0xff
    if k == 27: 
        break
      
  
cap.release() 
cv2.destroyAllWindows() 