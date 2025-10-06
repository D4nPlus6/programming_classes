def car(l):
    assert(isinstance(l,list)) 
    inv = l                    #pre-cond
    assert((len(l)-1))

    result = l[0]
    assert(l == inv)            #invariant

    assert(len(inv) == len(l))
    assert(inv[0] == result)    #post-cond
    return result

def cdr(l):
    assert(isinstance(l,list))  #pre-cond
    inv = l

    result = l[1:]
    assert(l == inv)            #invar

    assert(len(result) == (len(l)-1))
    assert(inv[1:] == result)   #post-cond
    return result

a = [2,4,6,8,10]
c1 = car(a)
c2 = cdr(a)
print(c1)
print(c2)

