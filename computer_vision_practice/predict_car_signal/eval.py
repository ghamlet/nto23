import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import pandas as pd





def key_control(*pictures):
    

    for i in range(len(pictures)):
        print(pictures[i])
        #cv2.imshow(f"{var_name(o)}", o)

    while True:


        global pos
        global breaking_bad

        
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
            return breaking_bad
            
       
pos = 0
breaking_bad = False

images = "images"
main_dir = os.path.dirname(__file__) #полный путь до файла
dir_images = os.path.join(main_dir, images) #путь до папки с фотографиями


csv = "annotations.csv"
csv_file = os.path.join(main_dir, csv)  #полный путь до таблицы ексель
data = pd.read_csv(csv_file, sep=';') #sep - разделитель
data = data.sample(frac=1) #парсинг данных таблицы
number_of_files = len(data) #количество фотографий



while True:
    if breaking_bad:
        break

    im, true_answer = list(enumerate(data.itertuples()))[pos][1][1:3]#из таблицы берем название файла
    frame_input = os.path.join(dir_images, im[7:] )#соединяем путь до папки с фотографиями с названием фотографии

    
    img = cv2.imread(frame_input)
    image = cv2.resize(img, (400, 300))
    
    img1 = image.copy()
    img2 = image.copy()

    red = cv2.inRange(image, (0, 0, 150), (120, 90, 255))
    yellow = cv2.inRange(image, (0, 80, 200), (120, 255, 255))
    
    result_red = cv2.bitwise_and(img1, img1,mask=red)
    result_yellow = cv2.bitwise_and(img2, img2,mask=yellow)

    orange_sum = np.sum(yellow)
    red_sum = np.sum(red)

    if orange_sum > red_sum:
        car_signal = "turn signal"
    else:
        car_signal = "stop signal"

    print(f"Ваш ответ: {car_signal} Правильный ответ: {true_answer}")

    while True:
        cv2.imshow('frame', img)
        
        cv2.imshow('result_yellow', result_yellow)
     
        
        
