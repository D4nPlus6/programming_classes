# inefficient O(N^2) time and O(1) space solution 🤮
# 1st of all, you're a disappointment for taking over 4 hours just to figure out an inefficient ahh solution
# 2nd of all, how could you procrastinate, over the SECOND EASIEST CODING PROBLEM SINCE THE BEGINNING OF THE COURSE
"""
N = int(input())
A = input().split()
B = input().split()

if N%2 != 0:
    print('bad')
    exit()

for i in range(N):
    a = A[i]
    b = B[i]
    if a == b:
        print("bad")
        exit()
    
    if B[A.index(b)] != a:
        print("bad")
        exit()

print("good")
"""

# hashmap approach O(N)
N = int(input())
A = input().split()
B = input().split()

if N%2 != 0:
    print('bad')
    exit()

# what in the mumbo jumbo is this 🤮
# pairing = {}
# for i in range(N):
#     a = A[i]
#     b = B[i]
#     if a == b:
#         print("bad")
#         break
#     try:
#         if pairing[b] == a:
            

            
#     except KeyError:
#         pairing.update({a:b})


# the mumbo jumbo I was tryna do lmao: (credits to https://www.youtube.com/watch?v=tfUYBH2OzAw)
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


