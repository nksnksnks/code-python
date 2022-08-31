import math

t = int(input())
while t>0 :
    a1 = input()
    b0 = list(reversed(a1))
    b1 = ''.join(b0)
    tes = 0
    sum = 0
    for i in range(0, len(a1)-1):
        if((ord(a1[i]) - ord(a1[i+1]) == ord(b1[i+1]) - ord(b1[i])) or (ord(a1[i]) - ord(a1[i+1]) == ord(b1[i]) - ord(b1[i+1]))):
            sum +=1
    if sum == len(a1)-1:
        print('YES')
    else:
        print('NO')
    t=t-1