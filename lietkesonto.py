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

n = int(input())
a = input()
a = a.split()
b = []
c= []
for i in range(0, len(a)):
    if(nt(int(a[i])) == 0):
        c.append(a[i])
        if c.count(a[i]) == 1:
            print(str(a[i]) + ' '+ str(a.count(a[i])))

