# -*- coding: utf-8 -*-

import cv2
import numpy 




def track_car(video) -> list:
    
    result = []
    bool_out_1, bool_out_2, bool_out_3, bool_out_4 = [False] * 4
    
    while True:  # цикл чтения кадров из видео
        
        status, frame = video.read()  # читаем кадр


        if not status:  # выходим из цикла, если видео закончилось
            break


        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h = hsv[:,:,0]
        

        in_2 = numpy.sum(h[ 270:280, 610:620])
        out_2 = numpy.sum(h[ 310:320, 540:550])

        in_3 = numpy.sum(h[ 580:690, 550:560])
        out_3 = numpy.sum(h[ 630:640, 610:620])

        in_1 = numpy.sum(h[ 290:300, 950:960])
        out_1 = numpy.sum(h[ 260:270, 880:890])
    

        in_4 = numpy.sum(h[ 610:620, 850:860])
        out_4 = numpy.sum(h[ 610:620, 950:960])


        
        if out_1 > 0:    
            bool_out_1 = True 

        elif out_2 > 0:
            bool_out_2 = True
   
        elif out_3 > 0:
            bool_out_3 = True
   
        elif out_4 > 0:
            bool_out_4 = True 
           
        

        elif in_1 > 0:

            if bool_out_2:
                result.append('l')
                bool_out_2 = False
            elif bool_out_3:
                result.append('s')
                bool_out_3= False
            elif bool_out_4:
                result.append('r')
                bool_out_4=False
    
            
        elif in_2 > 0:
            if bool_out_1:
                result.append('r')
                bool_out_1 = False
            elif bool_out_3:
                result.append('l')
                bool_out_3= False
            elif bool_out_4:
                result.append('s')
                bool_out_4=False
            
        
        elif in_3 > 0:
            if bool_out_1:
                result.append('s')
                bool_out_1 = False
            elif bool_out_2:
                result.append('r')
                bool_out_2= False
            elif bool_out_4:
                result.append('l')
                bool_out_4=False
              
            
        elif in_4 > 0:
            if bool_out_1:
                result.append('l')
                bool_out_1 = False
            elif bool_out_2:
                result.append('s')
                bool_out_2= False
            elif bool_out_3:
                result.append('r')
                bool_out_3=False
            
            
    return result 
    
