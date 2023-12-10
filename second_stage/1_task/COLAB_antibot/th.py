from threading import Thread
import cv2
import numpy as np
import random
import pyautogui
import time
import datetime

import logging
logging.basicConfig(level=logging.INFO, filename="second_stage/1_task/COLAB_antibot/pylog.log", filemode="w")


def wr_log():
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%d-%m %H:%M:%S")
    logging.info(f"пикча {current_date}")


def find_captcha():
    find = True

    while True:
        
        # pyautogui.moveTo(random.randint(200, 1700), random.randint(100, 900),3, pyautogui.easeInQuad)
        # pyautogui.scroll(random.randint(10, 1000))   
        # pyautogui.scroll(-random.randint(10, 1000))   

        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY) 

        _, threshold = cv2.threshold(gray, 20, 260, cv2.THRESH_BINARY) 
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
        
        for contour in contours: 
            area = cv2.contourArea(contour)

            if  22000 < area < 24000 and find:
                x,y,w,h = cv2.boundingRect(contour)
                if w < 1500:

                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.imwrite("ver.jpg", frame)
                    time.sleep(300)
                    pyautogui.moveTo(x+25, y+33,3)
                    pyautogui.click()
        
                    wr_log()
                    find = False
                    time.sleep(5)
                
            else: find = True
                
         
# def video():
#     global stop_thread
#     global find
    
#     resolution = (1920, 1080)
#     codec = cv2.VideoWriter_fourcc(*"XVID")
#     filename = "second_stage/1_task/COLAB_antibot/Recording.avi"
#     fps = 60.0
#     out = cv2.VideoWriter(filename, codec, fps, resolution)

#     while True:
        
#         img = pyautogui.screenshot()
#         frame = np.array(img)
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         out.write(frame)

#         if cv2.waitKey(1) == ord('q'):
#             break

#         if stop_thread:
#             find = True
#             break

#     out.release()
#     cv2.destroyAllWindows()





# thread_main.start()
# thread_main.join()


if __name__ == "__main__":

    # thread_video = Thread(target=video)
    # thread_main = Thread(target=find_captcha)

    # thread_main.start()

    # thread_video.join()
    # thread_main.join()
    
   
    find_captcha()