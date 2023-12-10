# -*- coding: utf-8 -*-
"""
Файл служит для определения точности вашего алгоритма
   Не редактируёте его!!!
   Для получения оценки точности, запустите файл на исполнение
"""

import eval
import cv2
import pandas as pd


def main():
    csv_file = "annotations.csv"
    data = pd.read_csv(csv_file, sep=';')
    data = data.sample(frac=1)

    correct = 0
    for i, row in enumerate(data.itertuples()):
        _, image_filename, true_signal = row

        image = cv2.imread(image_filename)

        user_signal = eval.predict_car_signal(image)

        if user_signal == true_signal:
            correct += 1

    total_object = len(data.index)
    print(f"Из {total_object} объектов верно детектированы {correct}")

    score = round(correct / total_object, 2)
    print(f"Точность: {score}")


if __name__ == '__main__':
    main()
