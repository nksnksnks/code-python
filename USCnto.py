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
    else:
        for i in range(2, a, 1):
            if a%i==0:
                test += 1 
    return test
t = int(input())
while t>0 :
    n,m = map(int,input().split())
    k = UCLN(n, m)
    k1 = str(k)
    length = len(str(k))
    sum = 0
    for i in range(0, length):
        sum += int(k1[i])
    if nt(sum) > 0:
        print('NO')
    else:
        print('YES')
    t=t-1