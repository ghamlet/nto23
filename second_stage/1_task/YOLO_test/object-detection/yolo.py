import cv2
import matplotlib.pyplot as plt
from utils import *
from darknet import Darknet
import os

# Set the NMS Threshold
score_threshold = 0.6
# Set the IoU threshold
iou_threshold = 0.4
cfg_file = "second_stage/1_task/YOLO_test/object-detection/cfg/yolov4-obj _2.cfg"
weight_file = "second_stage/1_task/YOLO_test/object-detection/data/yolov4-obj_best.weights"
namesfile = "second_stage/1_task/YOLO_test/object-detection/data/coco.names"
m = Darknet(cfg_file)
m.load_weights(weight_file)
class_names = load_class_names(namesfile)
# m.print_network()



files = os.listdir("C:/Users/max30/Desktop/videos/")
pos = 0

for _ in range(len(files)):
    cap = cv2.VideoCapture("C:/Users/max30/Desktop/videos/" + files[pos])
    
    while True:
        ret, frame = cap.read()
        

        original_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(original_image, (m.width, m.height))
        # detect the objects
        boxes = detect_objects(m, img, iou_threshold, score_threshold)
        # plot the image with the bounding boxes and corresponding object class labels
        plot_boxes(original_image, boxes, class_names, plot_labels=True)


