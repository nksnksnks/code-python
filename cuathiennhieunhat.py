t = int(input())
while t > 0:
    n = int(input())
    a = input()
    a = a.split()
    b = []
    c= []
    test = 0
    for i in range(len(a)-1): 
        b.append(a.count(a[i]))
        if b[i] > n/2:
            print(a[i])
            test +=1
            break
    if test == 0 and n > 1:
        print('NO')
    if n == 1:
        print(a[0])
    t-=1