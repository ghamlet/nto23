# -*- coding: utf-8 -*-
import cv2
import numpy


def predict_number_empty_parking_places(image): # просто название функции
 
  #cv2.imshow("frame", frame)

 cutedFrame = image[11:620, 20:420]
 #cv2.imshow("cutedFrame", cutedFrame)

 hsv = cv2.cvtColor(cutedFrame, cv2.COLOR_BGR2HSV)
 h= hsv[:,:,0]
 #cv2.imshow("h" +str(i), h)

 pervoemesto = numpy.sum(h[ 0:203, 0:420])
 vtoroemesto = numpy.sum(h[ 204:406, 0:420])
 tretyemesto = numpy.sum(h[ 407:609, 0:420])

 cv2.rectangle(cutedFrame, (0,0),(420,203),(0,0,255),3)
 cv2.rectangle(cutedFrame, (0,204),(420,406),(0,255,255),3)
 cv2.rectangle(cutedFrame, (0,407),(420,609),(0,255,0),3)
 #cv2.imshow("copy" +str(i), cutedFrame)

 #print(str(pervoemesto) + ":" + str(vtoroemesto) + ":" + str(tretyemesto))

 if pervoemesto == 0 and vtoroemesto == 0 and tretyemesto == 0:
  perking_places_list = [1,2,3]
 elif pervoemesto ==0 and vtoroemesto == 0:
  perking_places_list = [1,2]
 elif pervoemesto ==0 and  tretyemesto == 0:
  perking_places_list = [1,3] 
 elif vtoroemesto == 0 and  tretyemesto == 0:
  perking_places_list = [2,3] 
 elif  tretyemesto == 0:
  perking_places_list = [3]
 elif  pervoemesto == 0:
  perking_places_list = [1]
 elif  vtoroemesto == 0:
  perking_places_list = [2]
 elif pervoemesto > 0 and vtoroemesto > 0 and tretyemesto > 0:
  perking_places_list = []
 


   
    # Алгоритм проверки будет вызывать функцию predict_number_empty_parking_places,
    # остальные функции, если они есть, должны вызываться из неё.

   

 return perking_places_list
