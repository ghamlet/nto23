nums = input("n, m\n").split()
n,m = map(int, nums)

r = 0

while True:
    if n != m:
        if n < m:
            n += 3

        else:
            m += 7
        
        r += 1
    else:
        print(r)
        break

    