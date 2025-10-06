n = int(input())
nums = [int(input()) for i in range(n)]

def sumFactors(num):
    sums = [1]
    for i in range(2,(num//2)+1):
        if num/i%1 == 0:
            sums.append(i)
    
    return sum(set(sums))

for i in nums:
    factSum = sumFactors(i)
    if factSum == i:
        print(i,"is a perfect number.")
    if factSum > i:
        print(i,"is an abundant number.")
    if factSum < i:
        print(i,"is a deficient number.")
