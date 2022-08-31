import math
def UCLN(a, b):
    if(b==0):
        return a
    return UCLN(b, a%b)
m,n = map(int,input().split())
for i in range(m, n-1):
    for j in range(i+1, n):
        if UCLN(i, j) == 1:
            for z in range(j+1, n+1):
                if UCLN(j,z) == 1 and UCLN(z,i) == 1:
                    print('(' + str(i) + ', '+str(j) + ', ' + str(z)+')')
