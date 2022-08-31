import math
def UCLN(a, b):
    if(b==0):
        return a
    return UCLN(b, a%b)
n,k = map(int,input().split())
check = 0
check2 = 10
for i in range(10**(k-1), 10**k):
    if UCLN(n, i) == 1:
        check +=1
        if(check <=check2):
            print(str(i), end=(' '))
        else:
            print('')
            print(str(i), end=(' '))
            check = 1