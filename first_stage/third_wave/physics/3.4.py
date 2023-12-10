s = float(input("площадь главного зеркала "))
e = float(input("взв больше на сколько единиц "))

e2 = pow(100, (1/5))
e2 = e2 ** e
s2 = round(s * e2)
print(s2)