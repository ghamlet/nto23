# -*- coding: utf-8 -*-
"""
Файл служит для определения точности вашего алгоритма

Для получения оценки точности запустите файл на исполнение
"""

import eval as submission
import cv2
import pandas as pd


def check_answer(real_answer: list, user_answer: list) -> int:
    """
    return: amount of right answers
    """
    real_answer = real_answer[:]
    user_answer = user_answer[:]
    result = 0
    for real_detail in real_answer:
        if not user_answer:
            break
        user_detail = user_answer.pop(0)
        if real_detail == user_detail:
            result += 1

    return result


def main():
    csv_file = "engineering_tour/4_task/annotations.csv"
    data = pd.read_csv(csv_file, sep=',', dtype=str)
    data = data.sample(frac=1)

    total_correct = 0
    total_object = 0
    total_wrong = 0
    for i, row in enumerate(data.itertuples()):
        row_id, video_filename, real_label = row

        print(video_filename)
        video_filename = "C:/Users/max30/Desktop/NTO_2023_task4_user/" + video_filename
        # convert string of 0 and 1 to list
        real_label = list(real_label)

        total_object += len(real_label)

        video = cv2.VideoCapture(video_filename)
        user_answer = submission.track_car(video)
        
        video.release()
        
        wrong = 0
        if len(user_answer) > len(real_label):
            wrong = len(user_answer) - len(real_label)

        correct = check_answer(real_label, user_answer)
        total_correct += correct
        total_wrong += wrong

        print("Правильный ответ:", real_label)
        print("Ваш ответ:", user_answer)
        print(f'Верно определены {correct/(len(real_label) + wrong)*100:.1f}%')
        print()

    print(f"Из {total_object + total_wrong} предсказаний верны {total_correct}") #а тут не ошибка?

    score = total_correct / (total_object + total_wrong)
    print(f"Точность: {score:.2f}")


if __name__ == '__main__':
    main()