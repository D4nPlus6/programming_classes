J = int(input())
A = int(input())
jerseys = {}
for i in range(J):
    iptS = input()
    jerseys[i+1] = iptS

demands = set()
for i in range(A):
    iptD = input().split()
    demands.add((int(iptD[1]),iptD[0]))


occupied = set()
satisfCt = 0
for i in demands:
    dmNm = i[0]
    dmS = i[1]

    if dmNm not in occupied:
        if jerseys[dmNm] == dmS:
            satisfCt += 1
            occupied.add(dmNm)

        elif (jerseys[dmNm] == 'L' or jerseys[dmNm] == 'M') and (dmS == 'M' or dmS == 'S'):
            satisfCt += 1
            occupied.add(dmNm)

print(satisfCt)



