# -*- coding: utf-8 -*-
"""
Файл служит для определения точности вашего алгоритма
   Не редактируёте его!!!
   Для получения оценки точности, запустите файл на исполнение
"""

import eval
import cv2
import pandas as pd
from pathlib import Path
import pickle


def main():
    csv_file = "annotations.csv"
    data = pd.read_csv(csv_file, sep=';')
    data = data.sample(frac=1)

    correct = 0
    for i, row in enumerate(data.itertuples()):
        _, image_filename, free_places = row # free_places который был не подходит

        image = cv2.imread(image_filename)

        user_answer = eval.predict_number_empty_parking_places(image)

        if str(user_answer) == free_places:
            correct += 1

    total_object = len(data.index)
    print(f"iz {total_object} obektov verno detektirovany {correct}") #русский язык не печатает

    score = round(correct / total_object, 2)
    print(f"tochnost: {score }")


if __name__ == '__main__':
    main()
