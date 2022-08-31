import math
def UCLN(a, b):
    if(b==0):
        return a
    return UCLN(b, a%b)
def nt(a):
    test = 0
    if a==1:
        return 1
    if a==2 or a==3:
        return 0
    if a>3:
        for i in range(2, a, 1):
            if a%i==0:
                test += 1 
    return test
t = int(input())
while t>0 :
    n = int(input())
    k = 0
    for i in range(1, n):
        if UCLN(i, n) == 1:
            k+=1
    print(k)
    if nt(k) > 0:
        print('NO')
    else:
        print('YES')
    t=t-1