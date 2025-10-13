D = int(input("Number of starting donuts: "))
E = int(input("Number of events: "))
events = [input() for i in range(E*2)]

pointers = ['+','-']
for k,v in enumerate(events):
    if v in pointers:
        amountChange = events[k+1]
        if v == '+':
            D += int(amountChange)
        else:
            D -= int(amountChange)

print(D)
