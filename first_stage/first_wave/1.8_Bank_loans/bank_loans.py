

n = int(input())
#print("from to amount\n")
sum = 0
m =[]
case = []

for i in range(n):
    chain = input().split()
    chain = list(map(int, chain))
    m.append(chain)




for i in range(len(m)):
    
    case.append([m[i][1], m[i][2]]) #добавляем в массив пользователя с количеством денег
    

    if any(m[i][0] in sub for sub in case):
        
        value = m[i][0]
        #print(f"{value=}")

        send_sum = m[i][2]
        #print(f"{send_sum=}")


        for row in case:
            #print(f"{row=}")
            

            if value in row:
                #print("true")
                
                he_has = row[1]
                
                if send_sum > he_has:

                    unik = send_sum - he_has
                    sum += unik
                #else:
                    #print("Мы не можем утверждать, что транзакция уникальная")

    else:
        sum += m[i][2]
        
print(sum)


      