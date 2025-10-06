# algorithm O(N) for non-sorted array
arr = list(map(int, input().split()))
min = float('inf')
max = float('-inf')
for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i

print(min)
print(max)


