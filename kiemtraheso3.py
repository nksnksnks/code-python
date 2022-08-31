import math

t = int(input())
while t>0 :
    n = input()
    length = len(n)
    test = 0
    for i in range(0, length):       
        if n[i] > '2' or n[i] < '0':
            print("NO")
            break
        test +=1
    if test == length:
        print("YES")
    t=t-1
