import cv2

def load_models():
    print("load_models")

    config_path = "./yolov4tiny.cfg"  
    weights_path = "./yolov4tiny.weights"

    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
   

    yolo_model = cv2.dnn.DetectionModel(net)
    yolo_model.setInputParams(size= (256,256), scale= 1/255, swapRB=True)

    models = [yolo_model]
    return models


def count_vehicles(video, models):
    
    model = models[0]

    count_frame = 0
    center_points_prev_frame = []
    tracking_objects = {}
    track_id = 1   

    prev_len = 0

    while True:
        ret, frame = video.read()
        if not ret:
            break


        count_frame+=1
        center_points_cur_frame = []

        class_ids, scores, boxes = model.detect(frame, 0.2, 0.2)

        for box in boxes:
            
            (x,y,w,h) = box
           
            cx = int((x + x + w) / 2)
            cy = int((y + y + h) / 2)
            center_points_cur_frame.append((cx,cy))
            

        

        cur_len = len(boxes)
        if cur_len > prev_len: 
            if count_frame == 1: 
                for i in range(cur_len - prev_len):
                    
                        tracking_objects[track_id] = center_points_cur_frame[i]
                        track_id +=1
                
            else:
                
                for cur_pt in center_points_cur_frame:
                    for prev_pt in center_points_prev_frame:
                        
                        distance = ((prev_pt[0] - cur_pt[0])**2 + (prev_pt[1]  -cur_pt[1])**2 )**(1/2)
                        if distance < 150:
                           
                            for k, val in tracking_objects.copy().items():
                                if val == prev_pt:
                                    tracking_objects[k] = cur_pt
                            
               
                for item in center_points_cur_frame:
                    
                    if item not in tracking_objects.values():
                        tracking_objects[track_id] = item
                        track_id+=1

            prev_len = cur_len          


        elif cur_len == prev_len: 
            distances = []
            if cur_len != 0: 
                for cur_pt in center_points_cur_frame:
                   
                    must_find = 0
                    for prev_pt in center_points_prev_frame:
                        
                        distance = ((prev_pt[0] - cur_pt[0])**2 + (prev_pt[1]  -cur_pt[1])**2 )**(1/2)
                        if distance < 150: 
                            must_find = 0
                            distances.append(distance)
                            
                        else: must_find +=1

                    if must_find == cur_len: 
                        tracking_objects[track_id] = cur_pt
                        track_id += 1

                if len(distances) == cur_len:
                    for cur_pt in center_points_cur_frame:
                        for prev_pt in center_points_prev_frame:
                            distance = ((prev_pt[0] - cur_pt[0])**2 + (prev_pt[1]  -cur_pt[1])**2 )**(1/2)
                            if distance < 150:
                                for key, value in tracking_objects.copy().items():
                                    if value == prev_pt:
                                        tracking_objects[key] = cur_pt
                else:
                    distances = sorted(distances) 
                    
                    for cur_pt in center_points_cur_frame:
                        for prev_pt in center_points_prev_frame:
                            distance = ((prev_pt[0] - cur_pt[0])**2 + (prev_pt[1]  -cur_pt[1])**2 )**(1/2)
                            if distance in distances[0:cur_len]:
                                for key, value in tracking_objects.copy().items():
                                    if value == prev_pt:
                                        tracking_objects[key] = cur_pt


        elif cur_len < prev_len:
            for cur_pt in center_points_cur_frame:
                for prev_pt in center_points_prev_frame:
                    
                    distance = ((prev_pt[0] - cur_pt[0])**2 + (prev_pt[1]  -cur_pt[1])**2 )**(1/2)
                    if distance < 150:
                        for key, value in tracking_objects.copy().items():
                            if value == prev_pt:
                               
                                
                                tracking_objects[key] = cur_pt

            for id, item in tracking_objects.copy().items():    
                
                if item not in center_points_cur_frame: 
                    
                    car_in_centr = True if (item[0] > 50 and item[0] < 1700) and (item[1] < 900 and item[1] > 100) else False
                    if car_in_centr:
                        center_points_cur_frame.append(item)
                    else: 
                        tracking_objects.pop(id)

                    
            
            prev_len = len(center_points_cur_frame)       
                 


        center_points_prev_frame = center_points_cur_frame.copy()

  
    cars = track_id -1
    print(cars)
    return cars
        

       