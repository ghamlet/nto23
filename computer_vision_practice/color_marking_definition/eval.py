# -*- coding: utf-8 -*-
import cv2
## TODO: Допишите импорт библиотек, которые собираетесь использовать


def find_markers(image) -> list:
    image = cv2.imread(image)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    blue=cv2.inRange(hsv,(70,98,98),(155,255,255)) 
    cv2.imshow('blue', blue)
    
    green=cv2.inRange(hsv,(35,100,100),(85,255,255)) 
    cv2.imshow('green', green)

    yellow=cv2.inRange(hsv,(20,100,100),(30,255,255)) 
    cv2.imshow('yellow', yellow)

    red=cv2.inRange(hsv,(174,110,110),(178,255,255)) 
    cv2.imshow('red', red)

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
    cv2.imshow('gray', gray)
    

    ret,thresh=cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV) 
    cv2.imshow('thresh', thresh)
    cv2.waitKey(0)
    
    
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    contours=[cnt for cnt in contours if cv2.contourArea(cnt) > 10000] 
    bboxes=[cv2.boundingRect(cnt) for cnt in contours] 
    print(bboxes)
    answer=[] 

    for i,(x,y,w,h) in enumerate(bboxes):
        #box=hsv[y:y+h,x:x+w] 
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2) 
        cv2.putText(image,str(i),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0,255),2) 

        cnts=cv2.findContours(blue[y:y+h,x:x+w],cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts=cnts[0] if len(cnts)== 2 else cnts[1] 
        cnts=[cnt for cnt in cnts if 1000 < cv2.contourArea(cnt)<5000] 
        blue_slices=len(cnts) 
        print('blue:',blue_slices) 

        cnts=cv2.findContours(green[y:y+h,x:x+w],cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
        cnts=cnts[0] if len(cnts)== 2 else cnts[1] 
        cnts=[cnt for cnt in cnts if 1000 < cv2.contourArea(cnt) < 5000] 
        green_slices=len(cnts)
        print('green:',green_slices) 

        cnts=cv2.findContours(yellow[y:y+h,x:x+w],cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts=cnts[0] if len(cnts) == 2 else cnts[1] 
        cnts=[cnt for cnt in cnts if 1000 < cv2.contourArea(cnt) < 5000]
        yellow_slices=len(cnts) 
        print('yellow:',yellow_slices) 

        cnts=cv2.findContours(red[y:y+h,x:x+w],cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
        cnts=cnts[0] if len(cnts) == 2 else cnts[1]
        cnts=[cnt for cnt in cnts if 1000 < cv2.contourArea(cnt) < 5000] 
        red_slices=len(cnts) 
        print('red:',red_slices)

        print(f'answer for box {i}:',blue_slices+green_slices+yellow_slices+ red_slices) 
        answer.append(blue_slices+green_slices+yellow_slices+red_slices) 

        cv2.imshow('frame', image)
        cv2.waitKey(0)
    return sorted(answer)

find_markers("computer_vision_practice/color_marking_definition/images/4b7f4df6-62ac-4752-9ca8-29ace9a1216e.jpg")