cases = {1:100,2:500,3:1000,4:5000,5:10000,6:25000,7:50000,8:100000,9:500000,10:1000000}
n = int(input())
elim = [int(input()) for i in range(n)]
B = int(input())

for i in range(n):
    cases.pop(elim[i])

avg = sum(cases.values())/len(cases)
print('deal') if B > avg else print('no deal')

