def cyclelength(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count = count + 1
    return count

def maxcyclelength(i, j):
    if i < j:
        start = i
        end = j
    else:
        start = j
        end = i

    biggest = 0
    current = start
    while current <= end:
        length = cyclelength(current)
        if length > biggest:
            biggest = length
        current = current + 1

    return biggest

i = int(input())
j = int(input())
answer = maxcyclelength(i, j)
print(i, j, answer)

