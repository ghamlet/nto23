import cv2
import numpy as np
import pandas as pd
import os

from progress.bar import IncrementalBar
mylist = [*range(2,7304)]
bar = IncrementalBar('Countdown', max = len(mylist))


main_dir = os.path.dirname(__file__)


def read_data(): 
    csv_train_file = os.path.join(main_dir, "annotations_train.csv")
    data = pd.read_csv(csv_train_file, sep=',') 
    return data


def create_dataset(name_file, frame, size:tuple):
    if not os.path.isdir(main_dir+"/obj"):
        os.mkdir(main_dir+"/obj")

    cv2.imwrite(os.path.join(main_dir, f"obj/{name_file}.jpg"), frame)
    cv2.waitKey(1)

    with open(os.path.join(main_dir, f"obj/{name_file}.txt"), 'w') as file:
        txt = ' '.join(["0", str(size[0]), str(size[1]), str(size[2]), str(size[3])])
        file.write(txt)


def marking(x_max, x_min, y_max,y_min, width_video, height_video) -> tuple: 
    width_box = x_max - x_min
    height_box = y_max - y_min

    xc = round((x_min + width_box/2) / width_video, 4)
    yc = round((y_min + height_box/2) / height_video, 4)
    
    width_box = round(width_box / width_video, 4)
    height_box = round(height_box / height_video, 4)

    return (xc, yc, width_box, height_box)


def collect_data(data):
    current_video_file = None
    
    for i, row in enumerate(data.itertuples()):
        row_id, video_file, num_frame, x_min, y_min, x_max, y_max = row
        x_min, y_min, x_max, y_max = map(int,(x_min, y_min, x_max, y_max))
        name_file = row_id

        if video_file == current_video_file:
            bar.next()
            
            video.set(1, int(num_frame))  
            status, frame = video.read()

            size = marking(x_max, x_min, y_max,y_min, width_video, height_video )
            create_dataset(name_file, frame, size)  

            cv2.imshow('window_name', frame) 
            k = cv2.waitKey(1)
            
        else:
            current_video_file = video_file
            video = cv2.VideoCapture("C:/Users/max30/Desktop/videos/" + video_file[7:]) 

            width_video  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  
            height_video = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
              
    bar.finish()



def main():
    data = read_data()
    collect_data(data)
              

if __name__ == "__main__":
    main()    
           

