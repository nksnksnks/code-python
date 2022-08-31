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
    if nt(int(n[length-4:length])) == 0:
        print("YES")
    else:
        print("NO")
    t-=1