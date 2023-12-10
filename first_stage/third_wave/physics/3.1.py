v = float(input("скорость "))
a = float(input("сторона а "))
b = float(input("сторона b "))
d = float(input("сторона d "))
del_t = float(input("нагрев "))

c = 4200
ro = 1000
m = 1.67 * 10 **-27

n = (2 * c * del_t * (a * 10 ** -2) * (b * 10 ** -2) * (d * 10 ** -2 )) / (m * ((v * 10 **3) **2))
n = round(n / 10 **12)
print(n)