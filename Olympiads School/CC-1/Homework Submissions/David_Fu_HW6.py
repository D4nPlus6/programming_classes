from math import floor, ceil

costs = []
while True:
    n = int(input())
    if n == 0:
        break
    costs.append((n,[float(input()) for i in range(n)]))

def communism(n: int ,arr: list[float]) -> float:
    avg = sum(arr)/n

    distribRich = 0.0
    distribPoor = 0.0

    for i in arr:
        dif = i-avg
        if dif >= 0:
            distribRich += floor(dif * 100) / 100
        else:
            distribPoor += ceil(dif * 100) / -100

    return f"${round(max(distribPoor,distribRich),2)}"


for i in costs:
    print(communism(i[0],i[1]))

