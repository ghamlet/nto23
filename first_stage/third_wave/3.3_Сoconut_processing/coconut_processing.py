coconut = 0.5
container = 20

time = 0
count = 0

while True:
    
    time +=8
    count +=1
    massa = count * coconut

    print(f"{time=}")
    print(f"{massa=}")

    # if massa > container and time % 40:
    #     print(time)
    #     break
    
    if not (time % 40): 
        print("контейнер наполнился")
        if count == 45:
            print(time)
            break
        
        print(f"выгрузка - следующая в {time + 40}  {massa-2}")
        print(" ")
        count -=4

        

    
    

# 1480 - 185 момент 37  ,1504
#1440, 1472