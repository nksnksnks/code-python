import math
def UCLN(a, b):
    if(b==0):
        return a
    return UCLN(b, a%b)

n = int(input())
arrin = str(input())
arrin = arrin.split()
for i in range(0, n-1):
    for j in range(i+1, n):
        if int(arrin[i]) > int(arrin[j]):
            a = arrin[i]
            arrin[i] = arrin[j]
            arrin[j] = a
for i in range(0, n-1):
    for j in range(i+1, n):
        if UCLN(int(arrin[i]), int(arrin[j])) == 1:
            print(str(arrin[i]) + ' '+ str(arrin[j]))