import cv2
import dlib
import os
import pandas as pd


main_dir = (os.path.dirname(__file__))[:-4]
model_detector = dlib.simple_object_detector(os.path.join(main_dir,"SVM", "tld.svm"))
                                             
csv_file = os.path.join(main_dir, "annotations.csv")
data = pd.read_csv(csv_file, sep=',') 


for i, row in enumerate(data.itertuples()):
    row_id, video_filename, real_answer = row

    video = cv2.VideoCapture(os.path.join(main_dir, video_filename))

    while True:

        status, frame = video.read()
        if not status:
            break

        boxes = model_detector(frame)

        if boxes:
            print(video_filename)

        for box in boxes:
            (x,y,xb,yb) = [box.left(), box.top(), box.right(), box.bottom()]
            cv2.rectangle(frame, (x,y), (xb, yb), (255,0,255),2)

        cv2.imshow("frame", frame)

        k = cv2.waitKey(1)
        if k == 27:
            exit()
        elif  k == ord("q"):
            break
    