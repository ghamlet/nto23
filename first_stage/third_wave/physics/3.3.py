import math

v = float(input("максимальная скорость "))
a = float(input("максимальное ускорение "))
r = float(input("радиус окружности "))

t1 =  math.sqrt(r / a)
speed = math.sqrt(r * a)
t2 = (math.pi * r) / (2 * speed)

time = round(2 * t1 + t2, 1)
print(time)