lines = int(input())

pairs = []
for i in range(lines):
    line = list(map(int, input().split(' ')))
    pairs.append((line[0],line[1]))

## Not working code, cuz I passed cycles as a param, thus keeping it outside of the recursion, 'cycles' didn't working and was at 2 for every value in the memo ##
# memo = {}
# def threeNPlusOne(n,cycles=1):
#     if n in memo:
#         return memo[n]

#     if n == 1:
#         return cycles
#     else:
#         if n % 2 == 0:
#             cycles = threeNPlusOne(n//2,cycles+1)
#         else:
#             cycles = threeNPlusOne(n*3+1,cycles+1)
#     memo[n] = cycles
#     return cycles

# maxCycLens = []
# for i in pairs:
#     tmp = [threeNPlusOne(j) for j in range(i[0],i[1]+1)]
#     print(tmp)
#     maxCycLens.append(max(tmp))
# print(maxCycLens)
# print(memo)

## Working code 👍, memo can honestly be global or a param here; thx to chatgpt (im scared for my future career prospectcs) ##
## for helping me to figure out why the 'cycles' wasn't working and was at 2 for every value in the memo                    ##
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
