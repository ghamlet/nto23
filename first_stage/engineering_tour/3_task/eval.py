# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math
# TODO: Допишите импорт библиотек, которые собираетесь использовать


def gradient(pt1,pt2):
    if (pt2[0]-pt1[0]) == 0:
        return 0
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])


def get_angle(image) -> int:

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5, 5),0)
    edges = cv2.Canny(gray, 50,150)

    rho = 1 
    theta = np.pi / 180  
    threshold = 15  
    min_line_length = 200  
    max_line_gap = 20  
    
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    
    height, width = image.shape[:2] 
    x1,y1,x2,y2 = lines[0][0]

    x_mid, y_mid = (x1 + x2) //2, (y1 + y2) //2

    pt1 = x_mid , y_mid
    pt2 = (x_mid + lines[0][0][2]) // 2, (lines[0][0][3] + y_mid) //2
    pt3 = x_mid-1 , -400 
    
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1,pt3)
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))

    if x1 == x2:
        angD = 0

    elif y1 <= y2:
       
        if ((x_mid <= width // 2 +5) or (x_mid <= width // 2 -5)) and ((y_mid >= height // 2 +5) or (y_mid >= height // 2 -5)):
            angD = 180 - angD
        elif ((x_mid >= width // 2 + 5) or (x_mid >= width // 2 - 5)) and ((y_mid <= height // 2 +5) or (y_mid <= height // 2 - 5)):
            angD = (-1) * angD

    elif y1 >= y2:
        if ((x_mid <= width // 2 +5) or (x_mid <= width // 2 -5)) and ((y_mid <= height // 2 +5) or (y_mid <= height // 2 - 5)):
            angD = (-1) * (180 - abs(angD))
        elif ((x_mid >= width // 2 + 5) or (x_mid >= width // 2 - 5)) and ((y_mid >= height // 2 +5) or (y_mid >= height // 2 -5)):
            angD = abs(angD)
    
    return angD
 

    


 


        
       
        
      
        
        
   
        
    
    







    