W = int(input())
N = int(input())
cars = [int(input()) for i in range(N)]

maxCars = 0
left,right = 0,1
for i in range(len(cars)):
    window = cars[left:right]
    if sum(window) <= W:
        maxCars += 1
    else:
        break
    
    if right >= 4:
        left += 1
        right += 1
    else:
        right += 1


print(maxCars)
