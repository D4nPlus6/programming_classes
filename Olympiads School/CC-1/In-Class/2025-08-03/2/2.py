N = int(input())
A = input().split()
B = input().split()

assert isinstance(N,int); assert len(N) > 1 and len(N) <= 30
assert isinstance(A,list); assert isinstance(B,list); assert len(A)==len(B)

output = "bad"
if N%2 != 0:
    assert output == "bad" or output == "good"
    print(output)
    exit()

INVA = A
INVB = B
pairing = {}
for i in range(N):
    a = A[i]
    b = B[i]
    assert a == INVA[i]
    assert b == INVB(i)

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

        assert INVA == A; assert INVB == B
        assert isinstance(pairing,dict)

assert output == "bad" or output == "good"

print("good")
