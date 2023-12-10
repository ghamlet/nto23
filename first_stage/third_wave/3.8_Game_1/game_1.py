str_1 = input().split()
amount, target = list(map(int, str_1))

numbers = input().split()
numbers = list(map(int, numbers))


uniq = numbers.copy()
answer = 0

max_num = max(numbers)

while True:
    if max_num == target:
        #print(max_num)
        break

    if max_num == 0:
        answer = -1
        break

    count = numbers.count(max_num) 
   
    if count >= 2:
        for _ in range(2):
            numbers.remove(max_num)

        numbers.append(max_num + 1)
        count_old = uniq.count(max_num)

        if count_old >= 2:
            answer+=2
        elif count_old == 1:
            answer+=1 
        max_num+=1
        
        

    else: max_num-=1


print(answer)
