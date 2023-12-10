cars, line = map(int, input().split())
track = [0] * 10000000

for _ in range(cars):
    entry, speed = map(int, input().split())
    exit = entry + (line // speed)
    track[entry] += 1 
    track[exit] -= 1 

max_cars = 0
current_cars = 0

for i in range(line):
    current_cars += track[i]
    max_cars = max(max_cars, current_cars)

print(max_cars)