# Dynamic input--get median of numbers
vals = []
while True:
    tmp = float(input())
    if tmp == 0:
        break
    vals.append(tmp)

vals.sort()
n = len(vals)
if n & 1 == 0:
    floorMed = (len(vals)>>1) - 1
    print((vals[floorMed]+vals[floorMed+1])/2)
else:
    print(vals[n-1])
