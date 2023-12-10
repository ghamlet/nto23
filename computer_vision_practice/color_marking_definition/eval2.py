""""В представленном решении детектирование груза и распознавание маркировки выполняются 
раздельно. Детектирование осуществляется SVM-детектором, обученном на предоставленных тестовых 
изображениях. Для распознавания цветовой маркировки на детектированном грузе изображение 
разбивается на области, соответствующие возможным положениям полос. В каждой области
подсчитывается число пикселей конкретного цвета. Каких пикселей больше, таков и цвет полосы.
Определение пороговых значений составляющих цвета пикселей для различных цветов необходимо
подобрать путём экспериментов. Подбирать пороги можно в различных цветовых пространствах.
В приведённом решении используется цветовое простран- ство HSV."""


import cv2
import dlib
import numpy as np

def convert_and_trim_bb(image, rect):
    # extract the starting and ending (x, y)-coordinates of the
    # bounding box
    startX = rect.left()
    startY = rect.top()
    endX = rect.right()
    endY = rect.bottom()
    # ensure the bounding box coordinates fall within the spatial
    # dimensions of the image
    startX = max(0, startX)
    startY = max(0, startY)
    endX = min(endX, image.shape[1])
    endY = min(endY, image.shape[0])
    # compute the width and height of the bounding box
    w = endX - startX
    h = endY - startY
    # return our bounding box coordinates
    return startX, startY, w, h

def load_detector():
    """Функция осуществляет загрузку модели машинного обучения из файла.
    Выходные параметры: список загруженных моделей

    Если вы не собираетесь использовать эту функцию, пусть возвращает пустой
    список []
    Если вы используете несколько моделей, возвращайте их список [detector1,
    detector2]

    То, что вы вернёте из этой функции, будет передано вторым аргументом в функцию
    predict_box"""
    detectors_list  =  dlib.simple_object_detector('detector.svm')
    return detectors_list


def predict_colors_of_bars(image, detectors_list) -> tuple:
    """
    Функция, расшифровывающая цветовую маркировку на грузе
    Полосы могут быть четырёх цветов
    (синий - B, фиолетовый - M, зелёный - G, чёрный - 0)
    Чёрный цвет первой полосы всегда заменяется на жёлтый, обозначение "0" не
    меняется.

    Входные данные: изображение (bgr), список загруженных моделей
    Выходные данные: три символа, обозначающие соответствующием полос маркировки

    Примеры вывода:
    BMG - первая полоса голубая, вторая - фиолетовая, третья - зеленая;
    G0B - первая полоса зеленая, вторая - черная, третья - голубая;
    000 - все три полосы черные;
    """

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    rects = detectors_list(rgb_image)
    boxes = [convert_and_trim_bb(image, rect) for rect in rects]

    box = boxes[0]
    x1, y1, w, h = box
    x2, y2 = x1 + w, y1 + h
    line_w = int(w / 4)

    box_img = image.copy()[y1:y2, x1:x2]
    lines = []
    for i in range(3):
        lines.append(box_img[:, line_w * i:line_w * (i + 1)])

    result = ''

    for i, line in enumerate(lines):
        hsv = cv2.cvtColor(line, cv2.COLOR_BGR2HSV)

        line_black = cv2.inRange(hsv, (0, 0, 0), (179, 50, 50))
        line_yellow = cv2.inRange(hsv, (40, 100, 60), (65, 255, 255))
        line_magenta = cv2.inRange(hsv, (150, 100, 60), (179, 255, 255))
        line_green = cv2.inRange(hsv, (70, 100, 60), (90, 255, 255))
        line_blue = cv2.inRange(hsv, (90, 100, 50), (110, 255, 255))

        colors = ['black', 'yellow', 'magenta', 'green', 'blue']
        colors_values = [np.sum(line_black), np.sum(line_yellow),
        np.sum(line_magenta), np.sum(line_green),
        np.sum(line_blue)]

        color_index  =  colors_values.index(max(colors_values))
        color = colors[color_index]

        if color in ('black', 'yellow'):
            result	+= '0'
        elif  color	== 'magenta':
            result	+= 'M'
        elif  color	== 'green':
            result	+= 'G'
        elif  color	== 'blue':
            result	+= 'B'
        
    return result	
