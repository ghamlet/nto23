# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math
def distances(contour1, contour2):
    x1, y1, w1, h1 = cv2.boundingRect(contour1)
    x2, y2, w2, h2 = cv2.boundingRect(contour2)
    center1 = (x1 + w1 // 2, y1 + h1 // 2)
    center2 = (x2 + w2 // 2, y2 + h2 // 2)
    distance = np.sqrt((center2[0] - center1[0])**2 + (center2[1] - center1[1])**2)
    return distance

def measure_distance(image) -> float:
    
    my_photo = image
    img_grey =cv2.cvtColor(my_photo,cv2.COLOR_BGR2GRAY)
    img_grey = cv2.Canny(my_photo,100,200)

    thresh = 100

    #get threshold image
    ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

    #find contours
    contours = []
    cnt, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for c in cnt:
        if len(c)> 210:
            contours.append(c)

    contours = sorted(contours, key= cv2.contourArea,reverse=True)

    max_dist = 0
    for i in range(len(contours)):
        for j in range(i+1, len(contours)):
            distance = distances(contours[i],contours[j])
            if distance> max_dist:
                max_dist = distance
                n = i           
                m = j

    min_dist = 1000

    for cnt_1 in contours[m]:
        x1, y1 = cnt_1[0]
        for cnt_2 in contours[n]:
            x2,y2 = cnt_2[0]
            dist = np.sqrt((x1-x2)**2+(y1-y2)**2)
            if dist < min_dist:
                min_dist = dist
                min_dist = float(min_dist)           
    return min_dist