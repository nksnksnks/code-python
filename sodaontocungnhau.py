import math
def UCLN(a, b):
    if(b==0):
        return a
    return UCLN(b, a%b)
t = int(input())
while t>0 :
    a1 = input()
    b0 = list(reversed(a1))
    b1 = ''.join(b0)

    if UCLN(int(a1), int(b1)) == 1:
        print('YES')
    else:
        print('NO')
    t=t-1