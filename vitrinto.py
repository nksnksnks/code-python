import math

def nt(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
t = int(input())
while t>0 :
    n = input()
    length = len(n)
    test = 0
    for i in range(0, length):
        if (nt(int(n[i]))) == True and nt(i) == True:
            test+=1
        if (nt(int(n[i]))) == False and nt(i) == False:
            test+=1
    if test == length:
        print("YES")
    else:
        print("NO")
    t=t-1