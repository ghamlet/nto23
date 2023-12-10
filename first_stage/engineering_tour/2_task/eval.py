# -*- coding: utf-8 -*-
import cv2
import numpy as np
# TODO:


def count_contours(image) -> int:
    colors = []
    for bgr in range(3):

        kumar = [0] * 256
        base = image[2, 2, bgr]
        #print(base)
        height, width = image.shape[:2]
        for h in range(height):
            for w in range(width):
                pixel = image[h, w, bgr]
                if pixel != base:
                # if pixel not in kumar:
                    kumar[pixel]+=1

        ans = 0
        
        kumar = set(kumar)
        #kumar = sorted(kumar , reverse=True)
        #print(kumar)
        
        middle = sum(kumar) / len(kumar)-1
        #print(middle)

        for value in kumar:
            if  middle - 600 < value:
                ans+=1
        
        colors.append(ans)

    max_val = max(colors)
    
    return max_val