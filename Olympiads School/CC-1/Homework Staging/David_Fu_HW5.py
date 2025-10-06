inputs = []
while True:
    l = list(map(int,input().split()))
    if l == [0,0]:
        break

    assert(l[0] >= 1 and l[0] <= 10); assert(l[1] >= 0 and l[1] <= 99999999) #assert

    inputs.append(l)

assert isinstance(inputs,list) #assert
assert([0,0] not in inputs) #assert
assert False not in [False for i in inputs if len(i)!=2 or not (i[0] >= 1 and i[0] <= 10) or not (i[1] >= 0 and i[1] <= 99999999)] #assert


def prepScr(s,nlen):

    assert isinstance(s,int); assert isinstance(nlen,int) #assert
    assert(s >= 1 and s <= 10); assert(nlen >= 1 and nlen <= 8) #assert

    arr = [[] for i in range(2*s+3)]

    assert len(arr) == 2*s+3 #assert

    for i in range(2*s+3):
        for j in range(nlen):
            arr[i]+=(['A']*(s+2)+[' '])
        arr[i].pop()

        assert len(arr[i]) == nlen*((s+2)+1) - 1 #assert

    assert len(arr) == 2*s+3 #assert

    return arr


def dispDgt(scr,num,sz,idx):

    assert isinstance(scr,list); assert isinstance(scr[0],list); assert len(scr) >= 5 and len(scr) <= 23; assert len(scr[0]) >= 3 and len(scr[0]) <= 12 #assert
    assert isinstance(num,str); assert len(num) == 1 #assert

    if num == "1":
        for i in range(len(scr)):
            assert scr[i][idx+sz+2] == " " #assert

            if  
            # if (some statement with the i value to see if this should be a blank space or a '|')
            # scr[i][idx+sz+1] = '|'



for i in inputs:
    assert isinstance(i,list); assert len(i) == 2 #assert
    assert i[0] >= 1 and i[0] <= 10; assert i[1] >= 0 and i[1] <= 99999999 #assert

    num = str(i[1])
    scr = prepScr(i[0],len(num))

    #testing
    """
    # print(f"columns: {len(scr[0])}; rows: {len(scr)}")
    # for j in scr:
    #     print(''.join(j))
    """
    
    index = 0
    for j in range(len(num)):
        dispDgt(scr,j,i[0],index)

    for j in scr:
        print(''.join(j))
    print("\n")

    
