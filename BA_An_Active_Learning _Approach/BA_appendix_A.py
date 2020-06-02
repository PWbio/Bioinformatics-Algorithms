def min2 (a,b):
    if a>b:
        return b
    else:
        return a
min2(3,5)

def min3 (a,b,c):
    if a>b:
        return min2(b,c)
    else:
        return min2(a,c)
min3(1,2,3)

def min3_oneline(a,b,c):
    return min2(min2(a,b),c)
min3_oneline(1,3,5)

def min4 (a,b,c,d):
    if a>b:
        return min(b,c,d)
    else:
        return min(a,c,d)
min(2,4,6,8)

def min4_oneline (a,b,c,d):
    return min2(min3(a,b,c),d)
min(4,1,3,7)

def add(x,*args):
    for i in args:
        x = x + i
    return x
add(1,2,3,4)

#update git