n = int(input())

blue= list(map(int, input().split()))
red= list(map(int, input().split()))

red.sort(reverse=True)
blue.sort()

count=0
power_red=0
power_blue=0

for i in range(n):
    power_red += red[i]
    power_blue += blue[i]

    if power_blue<power_red:
        count+=1
        
print(count)