import cv2
import numpy as np
import math

import os

Conf_threshold = 0.2
NMS_threshold = 0.2



config_path = "second_stage/1_task/YOLO_test/object-detection/cfg/yolov4-tiny-obj.cfg"  # конфигурация нейронной сети
weights_path = "second_stage/1_task/YOLO_test/object-detection/data/yolov4-tiny-obj_best.weights"


net = cv2.dnn.readNetFromDarknet( config_path,weights_path)
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

model = cv2.dnn.DetectionModel(net)
model.setInputParams(size= (256,256), scale= 1/255, swapRB=True)
models = [model]

files = os.listdir("C:/Users/max30/Desktop/videos/")




for pos in range(len(files)):

    cap = cv2.VideoCapture("C:/Users/max30/Desktop/videos/" + files[pos])

    # cars = 0
    # prev_cars = 0


    count_frame = 0
    center_points_prev_frame = []
    tracking_objects = {}
    track_id = 1    #никто не считает машины с 0

    prev_len = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break


        count_frame+=1
        center_points_cur_frame = []

        class_ids, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)

        for box in boxes:
            
            (x,y,w,h) = box
            print(f"FRAME № {count_frame} ", x,y,w,h)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,255), 2)
            cx = int((x + x + w) / 2)
            cy = int((y + y + h) / 2)
            center_points_cur_frame.append((cx,cy))
            

        

        cur_len = len(boxes)
        if cur_len > prev_len: #появилась машина
            if count_frame == 1: #на первом кадре не с чем сопоставить текущий кадр поэтому все найденные машины добавляем в детекшэн
                for i in range(cur_len - prev_len):
                    #должны проверить прошлые координаты и добавить в tracking_objects машину которой нет на прошлом кадре
                    
                        tracking_objects[track_id] = center_points_cur_frame[i]
                        track_id +=1
                
            else:
                
                for cur_pt in center_points_cur_frame:
                    for prev_pt in center_points_prev_frame:
                        
                        distance = math.hypot(prev_pt[0] - cur_pt[0], prev_pt[1]  -cur_pt[1])
                        if distance < 150: #нашлась пара координат из текущего кадра и прошлого
                            #надо перезаписать трекинг
                            for k, val in tracking_objects.copy().items():
                                if val == prev_pt:
                                    tracking_objects[k] = cur_pt
                            
                print(tracking_objects)
                for item in center_points_cur_frame:
                    
                    if item not in tracking_objects.values():
                        tracking_objects[track_id] = item
                        track_id+=1

            prev_len = cur_len          


        elif cur_len == prev_len: #надо проерить одни и теже ли это машины
            if cur_len != 0: #если кадры пустые то скипаем
                for cur_pt in center_points_cur_frame:
                    for prev_pt in center_points_prev_frame:
                        
                        distance = math.hypot(prev_pt[0] - cur_pt[0], prev_pt[1]  -cur_pt[1])
                        if distance < 150:
                            for key, value in tracking_objects.copy().items():
                                if value == prev_pt:
                                    tracking_objects[key] = cur_pt



                


        elif cur_len < prev_len: #забыл добавить трекинг
            for cur_pt in center_points_cur_frame:
                for prev_pt in center_points_prev_frame:
                    
                    distance = math.hypot(prev_pt[0] - cur_pt[0], prev_pt[1]  -cur_pt[1])
                    if distance < 150:
                        for key, value in tracking_objects.copy().items():
                            if value == prev_pt:
                                tracking_objects[key] = cur_pt

            for item in tracking_objects.values():    
                if item not in center_points_cur_frame:
                    center_points_cur_frame.append(item)
            
            prev_len = len(center_points_cur_frame)       
                 


        for object_id, pt in tracking_objects.items():
            cv2.circle(frame, pt, 5, (255,0,255), -1)
            cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (255,0,255), 2)

        print("CUR FRAME")
        print(center_points_cur_frame)

        print("PREV FRAME")
        print(center_points_prev_frame)
         
        print("Tracking objects")
        print(tracking_objects, "\n")

        center_points_prev_frame = center_points_cur_frame.copy()


        frame = cv2.resize(frame, (640,640))
        cv2.imshow("frame", frame)

        key = cv2.waitKey(0)
        if key == ord("q"):
            exit(0)

        elif key == ord("d"):
            pos+=1
            break
        

       #print(cars)

cap.release
cv2.destroyAllWindows()

