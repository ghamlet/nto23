print("x y z w e")
count = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for e in range(2):

                    f1 = (not(y) or (y and not(z)) and (y or not(e))) <= (x and w or not(w) and x)
                    
                    f2 = ((not(x) or not(y) or not(z)) and (x or y and z)) and (not(w) or (e and w or w and not(e)))

                    if f1 != f2:
                        count+=1


print(count)