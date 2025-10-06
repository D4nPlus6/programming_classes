lines = int(input())

pairs = []
for i in range(lines):
    line = list(map(int, input().split(' ')))
    pairs.append((line[0],line[1]))


def threeNPlusOne(n,memo={1:1}):
    if n in memo:
        return memo[n]

    if n % 2 == 0:
        cycles = 1 + threeNPlusOne(n//2,memo)
    else:
        cycles = 1 + threeNPlusOne(n*3+1,memo)

    memo[n] = cycles
    return cycles


maxCycLens = []
for i in pairs:
    tmp = [threeNPlusOne(j) for j in range(i[0],i[1]+1)]
    maxCycLens.append(max(tmp))

for i in range(len(pairs)):
    print(pairs[i][0],pairs[i][1],maxCycLens[i])

    