n = int(input())
nums = [int(input()) for i in range(n)]

def divByElevAlgo(num):
    Num = list(str(num))
    while len(Num) >= 2:
        print("".join(Num))
        if Num[0] != '-' and len(Num) >= 2:
            rightmost = Num.pop()
            Num = list(str( int("".join(Num)) - int(rightmost) ))

        else:
            return int("".join(Num))
    
    return int("".join(Num))

for i in nums:
    if divByElevAlgo(i)/11%1 == 0:
        print(f"The number {i} is divisible by 11.")
    else:
        print(f"The number {i} is not divisible by 11.")

#testing
"""
n = int(input())
nums = [int(input()) for i in range(n)]

def divByElevAlgo(num):
    Num = list(str(num))
    while len(Num) >= 2:
        print("".join(Num))
        if Num[0] != '-' and len(Num) >= 2:
            rightmost = Num.pop()
            Num = list(str( int("".join(Num)) - int(rightmost) ))

        else:
            return int("".join(Num))
    
    return int("".join(Num))

for i in nums:
    print(divByElevAlgo(i)/11%1==0,'|',i/11%1 == 0)
        
"""