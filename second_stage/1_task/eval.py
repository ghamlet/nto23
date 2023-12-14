# -*- coding: utf-8 -*-
from typing import Tuple

import cv2
import numpy as np



def load_models():

    config_path = "C:/Users/max30/Desktop/weights/Yolov4/yolov4_obj.cfg"  # конфигурация нейронной сети
    weights_path = "C:/Users/max30/Desktop/weights/Yolov4/yolov4_obj_best.weights "

    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    # net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    # net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    yolo_model = cv2.dnn.DetectionModel(net)
    yolo_model.setInputParams(size= (608,608), scale= 1/255, swapRB=True)

    models = [yolo_model]
    return models


def сount_vehicles(video, models) -> int:
    
    yolo_model = models[0]
    cars = 0
    prev_cars = 0

    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        classes, scores, boxes = yolo_model.detect(frame, 0.1, 0.1)
        cur_cars = len(boxes)
        
        
        if cur_cars >= prev_cars:
            cars += cur_cars - prev_cars
            prev_cars = cur_cars
        else:
            prev_cars = cur_cars




    return cars
  
    