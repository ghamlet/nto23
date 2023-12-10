
count = 0




for i in range(1,64):
    x = 2 ** i - 1
    for j in range(1,64):
        y = 2 ** j -1
        
        if x > y:
            """1) x > y"""
            print(f"{x=}, {y=}")
            count += 1


        """2) * """
        print(f"{x=}, {y=}")
        gen = x * y
        print(gen) #произведение

        binary_num = format(gen, 'b')
        print(binary_num) #в двоичной записи
        
        
        if len(set(str(binary_num))) == 2: #превращаем в строку и удаляем повторяющиеся символы
            count += 1
        

        """3) """
        c_0 = str(binary_num).count('0')
        print(f"{c_0=}")

        c_1 = str(binary_num).count('1')
        print(f"{c_1=}")

        if abs(c_1 - c_0) <= 13:
            count += 1
        

        
print(count)


        

        
        



