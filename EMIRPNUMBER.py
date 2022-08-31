import math
def nto(a):
    test = 0
    if a <2:
        test = 1
    if a < 4 and a>1:
        test = 0
    if a >=4:
        for i in range(2, int(math.sqrt(a))+1):
            if a%i==0:
                test+=1
                break
    return test
t = int(input())
while t > 0:
    n = input()
    test = 0
    for i in range(11, int(n), 2):
        if nto(int(i)) == 0:
            i0 = tuple(reversed(str(i)))
            i1 =''.join(i0)
            if nto(int(i1)) == 0 and int(i1) != int(i) and int(i1) < int(n) and int(i1) > i:
                print(str(i) + " " + str(i1), end=(' '))
    print('')
    t-=1
    
    


