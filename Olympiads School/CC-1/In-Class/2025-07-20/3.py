# dynamic input--get median of each line
lines = []
while True:
    tmp = list(map(float, input().split(' ')))
    if tmp == [0.0]:
        break
    lines.append(tmp)

def getMed(vals):
    n = len(vals)
    if n & 1 == 0:
        floorMed = (len(vals)>>1) - 1
        return (vals[floorMed]+vals[floorMed+1])/2
    else:
        return vals[n-1]

for i in range(len(lines)):
    # lines[i].sort() # silly mistake; read the darn question carefully: "...in increasing value..." means pre-sorted
    print(getMed(lines[i]))

