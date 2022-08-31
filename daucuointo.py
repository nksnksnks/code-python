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
    if (nt(int(n[length-4:length]))) == True:
        print("YES")
    else:
        print("NO")
    t=t-1