J = int(input())
A = int(input())
jerseys = {}
for i in range(J):
    iptS = input()
    jerseys[i+1] = iptS

# set cuz if two ppl demand same thing, can only fulfill one
demands = set()
for i in range(A):
    iptD = input().split()
    demands.add((int(iptD[1]),iptD[0]))


# set cuz if two ppl demand same num, can only fulfill one
occupied = set()
satisfCt = 0
for i in demands: # this was an easy diffculty question lmao
    dmNm = i[0]
    dmS = i[1]

    if dmNm not in occupied:
        if jerseys[dmNm] == dmS: #if demanded num and size match
            satisfCt += 1
            occupied.add(dmNm)

        # if demanded num match but size is larger than demanded
        elif (jerseys[dmNm] == 'L' or jerseys[dmNm] == 'M') and (dmS == 'M' or dmS == 'S'):
            satisfCt += 1
            occupied.add(dmNm)

print(satisfCt)





