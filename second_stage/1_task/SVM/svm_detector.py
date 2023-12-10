import cv2
import numpy as np
import pandas as pd
import dlib
import os

main_dir = (os.path.dirname(__file__))[:-4]
print(main_dir)


def read_data(): 
    csv_train_file = os.path.join(main_dir, "annotations_train.csv")
    data = pd.read_csv(csv_train_file, sep=',') 
    return data


def collect_data(data):
    current_video_file = None
    c = 0
    images = []
    annots = []

    for i, row in enumerate(data.itertuples()):
        row_id, video_file,num_frame,x_min,y_min,x_max,y_max = row
        
        if video_file == current_video_file: #в annotations_train.csv содержатся повторения названий видео
            #print("the same video")
            video.set(1, int(num_frame))  # second arg is the frame you want
            status, frame = video.read()

            if  1.5 < (int(x_max - int(x_min))) / (int(y_max) - int(y_min)) < 2.2:
                images.append(frame)
                annots.append([dlib.rectangle(left = int(x_min), top = int(y_min), right = int(x_max), bottom = int(y_max))])

            # cv2.rectangle(frame,(x_min,y_min),(x_max,y_max),(255,255,0),3)
            # cv2.imshow('window_name', frame)  # show frame on window
            # cv2.waitKey(0)

        else:
            current_video_file = video_file
            c+=1
            print(current_video_file)
            video = cv2.VideoCapture(os.path.join(main_dir, current_video_file)) # video_name is the video being called
        
        if c == 2:
            break
        
    return images, annots
    

def main():

    data = read_data()
    images, annots = collect_data(data)
    
    options = dlib.simple_object_detector_training_options()
    options.be_verbose = True
    detector = dlib.train_simple_object_detector(images, annots, options)
    detector.save(os.path.join(main_dir, "SVM","tld.svm")) 
    print("Detector Saved")          

if __name__ == "__main__":
    main()    
           

