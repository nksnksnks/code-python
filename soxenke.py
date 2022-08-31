import math

def test(n):
    test0 = len(n)
    if test0%2==0:
        return False
    if int(n[0]) == int(n[1]):
        return False
    for i in range(2, test0, 2):
        if int(n[i]) != int(n[i-2]):
            return False
    return True

t = int(input())
while t>0 :
    n = input()
    if test(n) == True:
        print("YES")
    else:
        print("NO")
    t=t-1