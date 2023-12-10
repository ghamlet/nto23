e = float(input("взв больше на сколько единиц "))
m = float(input("масса обьектива "))

e2  = pow(100, (1/5))
e2 = e2 ** e
r = pow(e2,(1/2))
v = r ** 3
m2 = m *10**-3 * v
m2 = round(m2 * 10 ** -3, 1)
print(m2)