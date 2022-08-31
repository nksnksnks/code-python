import math
def UCLN(a, b):
    if(b==0):
        return a
    return UCLN(b, a%b)
def nt(a):
    test = 0
    if a==1:
        test += 1
    if a==2 or a==3:
        test = 0
    if a>3:
        for i in range(2, math.floor(math.sqrt(a))):
            if a%i==0:
                test += 1 
                break
    return test
t = int(input())
while t>0 :
    n = int(input())
    k = 0
    for i in range(1, n):
        if UCLN(i, n) == 1:
            k+=1
    if nt(k) == 0:
        print('YES')
    else:
        print('NO')
    t=t-1