import cv2
import numpy as np
import time
import sys
import os

Conf_threshold = 0.1
NMS_threshold = 0.2
COLORS = [(0,255,0),(0,0,255),(255,0,0),(225,255,0),(255,0,255),(0,255,255)]

class_name = []

with open("second_stage/1_task/YOLO_test/object-detection/data/coco.names") as f:
    class_name = [cname.strip() for cname in f.readlines()]

config_path = "second_stage/1_task/YOLO_test/object-detection/cfg/yolov4-obj _2.cfg"  # конфигурация нейронной сети
weights_path = "second_stage/1_task/YOLO_test/object-detection/data/yolov4-obj_best.weights"  # файл весов сети YOLO


# загружаем сеть YOLO
net = cv2.dnn.readNet(weights_path, config_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

model = cv2.dnn.DetectionModel(net)
model.setInputParams(size= (608,608), scale= 1/255, swapRB=True)


files = os.listdir("C:/Users/max30/Desktop/videos/")


for pos in range(len(files)):
    cap = cv2.VideoCapture("C:/Users/max30/Desktop/videos/" + files[pos])
    starting_time = time.time()
    frame_counter = 0

    while True:
        ret, frame = cap.read()
        frame_counter+=1

        if not ret:
            break

        classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)
        for (classid, score, box) in zip(classes, scores, boxes):
            color = COLORS[int(classid) % len(COLORS)]

            label =  (class_name[classid], score)

            cv2.rectangle(frame, box, color, 1)
            cv2.putText(frame, str(label), (box[0], box[1]-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 1)


        endingTime = time.time() - starting_time
        fps = round(frame_counter / endingTime)
        cv2.putText(frame, f"FPS: {fps}", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        elif key == ord("d"):
            pos+=1
            break


cap.release
cv2.destroyAllWindows()

