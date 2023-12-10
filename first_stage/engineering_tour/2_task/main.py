# -*- coding: utf-8 -*-
"""
Файл служит для определения точности вашего алгоритма

Для получения оценки точности, запустите файл на исполнение
"""

import eval as submission
import cv2
import pandas as pd


def main():
    csv_file = "engineering_tour/2_task/annotations.csv"
    data = pd.read_csv(csv_file, sep=',')
    data = data.sample(frac=1)


    correct = 0
    print(enumerate(data.itertuples()))
    for i, row in enumerate(data.itertuples()):
        row_id, image_filename, real_contours = row

        image = cv2.imread("engineering_tour/2_task/" + image_filename)

        user_answer = submission.count_contours(image)

        if real_contours == user_answer:
            correct += 1
            print(image_filename, '- верно')
        else:
            print(image_filename, '- неверно')

    total_object = len(data.index)
    print(f"Из {total_object} предсказаний верны {correct}")

    score = correct / total_object
    print(f"Точность: {score:.2f}")


if __name__ == '__main__':
    main()