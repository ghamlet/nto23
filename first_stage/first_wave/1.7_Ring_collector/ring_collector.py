n = int(input())

chain = input().split()
chain = list(map(int, chain))
l = len(chain)
time = 0
pos = 0

m = {}
for i in range(n):
    m[chain[i]] = i



for cell in range(1, n+1):
    value_index = m[cell]

    if value_index < pos:
        time += l - pos + value_index
    else:
        time += value_index - pos
          
    pos = value_index
    
print(time)

    
    
