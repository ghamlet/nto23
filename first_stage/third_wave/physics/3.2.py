
#если концентрация в 10**18 м-3 то норм
n = float(input("концентрация без 10 со степенью "))
s = float(input("сечение "))
i = float(input("сила тока "))

s = s * 10 ** -6 
i = i * 10 ** -6
e = 1.6 * 10 **-19
n = n * 10 ** 18

v = i / (e * n * s)
v = round(v * 100)
print(v)