str_in = input().split()
door, types, ti = list(map(int, str_in))

keys = input().split()
keys = list(map(int, keys))


list_keys = [] #type :1,2,3 pos:index count

for type in range(1, types + 1):
    list_keys.append([type, float("inf"), 1]) # inf - infinity, by default you need one key


counter = 0
answer = []

for item in keys:
    counter += 1
    row = item - 1

    pos = list_keys[row][1]

    if counter - pos > ti:
        list_keys[row][2] += 1 
     
    list_keys[row][1] = counter

    
for ki in list_keys:
    answer.append(ki[2])
  

total = sum(answer)
print(total)
print(*answer)


            
    


