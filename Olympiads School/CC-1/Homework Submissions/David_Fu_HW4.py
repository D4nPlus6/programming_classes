N = int(input())
A = input().split()
B = input().split()

if N%2 != 0:
    print('bad')
    exit()

pairing = {}
for i in range(N):
    a = A[i]
    b = B[i]
    if a == b:
        print("bad")
        exit()
    try:
        if pairing[b] != a:
            print("bad")
            exit()  
    except KeyError:
        pairing.update({a:b})
        pairing.update({b:a})

print("good")
