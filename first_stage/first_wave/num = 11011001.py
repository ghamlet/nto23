num_input = "11011001"
binn= ""


def allBits(n):
    if n:
        yield from ( bits+bit for bits in allBits(n-1) for bit in ("0","1") )
    else: 
        yield ""

for bits in allBits(8):
    for q in range(127):

        for i in range(0, len(num_input)):
            if num_input[i] == bits[i]:
                binn = binn + "0"
            else:
                binn = binn + "1"
        

        
        print(f" k chislu {num_input} primenyetza XOR {bits} Poluchili {binn}")
        num_input = binn
        binn=""

        if num_input == "00100101":
            print("succes")
            break
    
