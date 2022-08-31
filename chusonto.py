import math
def nt(a):
    test = 0
    if a<2:
        test += 1
    if a==2 or a==3:
        test = 0
    if a>3:
        for i in range(2, int(math.sqrt(a))+1):
            if a%i==0:
                test += 1 
                break
    return test
t = int(input())
while(t>0):
    n = input()
    length = len(n)
    sum = 0
    sum1 = 0
    sum2 = 0
    for i in range(0, length):
        sum += 1
        if nt(int(n[i])) == 0:
            sum1+=1
        else:
            sum2+=1
    if nt(sum) == 0 and sum1 > sum2:
        print("YES")
    else:
        print("NO")
    t-=1