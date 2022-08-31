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
    sum = 0
    for i in range(0, length):
        if (int(n[i]))%2==0 and i%2==0:
            test+=1
        if (int(n[i]))%2==1 and i%2==1:
            test+=1
        sum += int(n[i])
    if test == length and nt(sum) == True:
        print("YES")
    else:
        print("NO")
    t=t-1