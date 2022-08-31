
def chia_7(n):
    test = 0
    for i in range(0, len(n)):
        test +=int(n[i])
        test *= 3
    if test % 7 == 0:
        return True
    else:
        return False
def cong(m, n):
    t = int(len(n))
    kitu = ''
    du = 0
    while t > 0:
        tong = int(m[t]) + int(n[t]) + int(du)
        du = 0
        if tong-10 >= 0 and t>1:
            du = 1
            kitu = str(tong-10)
            test += kitu
        if tong-10 < 0 and t>1:
            kitu= str(tong)
            test += kitu
        if t == 1 :
            kitu = str(tong-10)
        tong = 0
        t-=1
    newtest = list(reversed(kitu))
    new = ''.join(newtest)
    return new
t = int(input())
while t > 0:
    n = input()
    nsau = n
    n0 = list(reversed(n))
    n1 = ''.join(n0)
    test = 0
    for i in range(0, 1001):
        if chia_7(str(nsau)) == True:
            print(nsau)
            break
        nsau = cong(n, n1)
        test = i
    if test > 999:
        print('-1')
    t-=1
    

