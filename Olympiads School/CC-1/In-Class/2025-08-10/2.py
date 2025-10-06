# guessing game based on binary search
N = int(input())
Max = N
Min = 0

count = 0
while True:
    mid = (Min+Max)//2 
    print(mid)
    choice = input()
    if choice == "correct answer":
        break
    elif choice == "too low":
        Min = mid+1
    elif choice == "too high":
        Max = mid-1

    count+=1
    
print(count)