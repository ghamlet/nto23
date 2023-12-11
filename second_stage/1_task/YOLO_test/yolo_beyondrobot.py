import cv2
import numpy as np
import math

import os

Conf_threshold = 0.1
NMS_threshold = 0.2
COLORS = [(0,255,0),(0,0,255),(255,0,0),(225,255,0),(255,0,255),(0,255,255)]

class_name = []

with open("second_stage/1_task/YOLO_test/object-detection/data/coco.names") as f: 
    class_name = [cname.strip() for cname in f.readlines()]

config_path = "d:/weights/Yolov4/yolov4-obj.cfg"  # конфигурация нейронной сети
weights_path = "d:/weights/Yolov4/yolov4-obj_best.weights "


# загружаем сеть YOLO
net = cv2.dnn.readNet(weights_path, config_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

model = cv2.dnn.DetectionModel(net)
model.setInputParams(size= (608,608), scale= 1/255, swapRB=True)


files = os.listdir("d:/videos")

counter = 0
center_points_prev_frame = []
tracking_objects = {}
track_id = 0

for pos in range(len(files)):
    cap = cv2.VideoCapture("d:/videos/" + files[pos])
    

    while True:
        ret, frame = cap.read()
        counter+=1
        if not ret:
            break

        center_points_cur_frame = []

        classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)
      
        for box in boxes:
            (x,y,w,h) = box
            cx = int((x + x + w) / 2)
            cy = int((y + y + h) / 2)
            center_points_cur_frame.append((cx, cy))


        
        if counter <= 2:
            for pt in center_points_cur_frame:
                for pt2 in center_points_prev_frame:
                    distance = math.hypot(pt2[0] - pt[0], pt2[1]  -pt[1])
                    print(distance)

                    if distance < 150:
                        tracking_objects[track_id] = pt
                        track_id +=1
        else:
            for pt in center_points_cur_frame:
                for object_id, pt2 in tracking_objects.items():
                    distance = math.hypot(pt2[0] - pt[0], pt2[1]  -pt[1])
                    if distance < 150:
                        tracking_objects[object_id] = pt


        for object_id, pt in tracking_objects.items():
            cv2.circle(frame, pt, 5, (255,0,255), -1)
            cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0,1, (255,0,255), 2)


            

        print(tracking_objects)
        center_points_prev_frame = center_points_cur_frame.copy()



           

        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            exit(0)

        elif key == ord("d"):
            pos+=1
            break


cap.release
cv2.destroyAllWindows()

