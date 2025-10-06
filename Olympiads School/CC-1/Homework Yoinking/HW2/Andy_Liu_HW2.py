num_input = int(input())
results = []

for x in range(num_input):
    i, j = map(int, input().split())
    n_list= []
    for x in range(i, j+1):
        n = 0
        while x != 1:
            if x % 2 == 0:
                x = x/2
            else:
                x = 3*x+1
            n+=1
        n+=1
        
        
        n_list.append(n)
    n_max = max(n_list)
    results.append(f"{i} {j} {n_max}")
    
for x in results:
    print(x)
