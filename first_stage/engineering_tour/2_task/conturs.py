
"""ЧТОБЫ НИЧЕГО НЕ МЕНЯТЬ МОЖНО ЗАКИНУТЬ ЭТОТ ФАЙЛ В ОДНУ ДИРЕКТОРИЮ С ПАПКОЙ ФОТОГРАФИЙ"""
import cv2
import numpy as np
import math
import os
import pandas as pd

 
pos = 0 
breaking_bad = False

images = "images"

main_dir = os.path.dirname(__file__) #полный путь до файла
dir_images = os.path.join(main_dir, images) #путь до папки с фотографиями

csv = "annotations.csv"
csv_file = os.path.join(main_dir, csv)  #полный путь до таблицы ексель
data = pd.read_csv(csv_file, sep=',')
data = data.sample(frac=1) #парсинг данных таблицы
number_of_files = len(data) #количество фотографий


while True:

    if breaking_bad:
        break

    img = list(enumerate(data.itertuples()))[pos][1][1] #из таблицы берем название файла
    frame_input = os.path.join(dir_images, img[7:] )#соединяем путь до папки с фотографиями с названием фотографии
    
    #дальше обычная прога
    frame = cv2.imread(frame_input)

    kumar = [0] * 256
    base = frame[2, 2, 2]
    print(base)
    height, width = frame.shape[:2]
    for h in range(height):
        for w in range(width):
            pixel = frame[h, w, 2]
            if pixel != base:
            # if pixel not in kumar:
                kumar[pixel]+=1

    ans = 0
    kumar = set(kumar)
    #kumar = sorted(kumar , reverse=True)
    #print(kumar)
    
    middle = sum(kumar) / len(kumar)-1
    print(middle)

    for value in kumar:
        if  middle - 400 < value:
            ans+=1
    print(ans)
    
    
    true_ans = list(enumerate(data.itertuples()))[pos][1][2] # берем правильный ответ из таблицы
    print(f"{img[7:]} {ans} {true_ans=}")
        
    
    
    while True:
        cv2.imshow('frame', frame)
       

        k = cv2.waitKey(1)

        if k == ord('a'):
            pos=pos-1

            if pos < 0:
                pos = 0
                print("the first file is open")
            else: cv2.destroyAllWindows()
            break
        
        
        elif k == ord('d'):
            pos=pos+1
            

            if pos == number_of_files:
                pos = number_of_files - 1
                print("files are over")
            else: cv2.destroyAllWindows()
            break

        elif k == ord('q'):
            cv2.destroyAllWindows()
            breaking_bad = True
            break

    