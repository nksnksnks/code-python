t = int(input())
while t>0:
    n = input()
    length = len(n)
    sum = 0
    product = 1
    test = 0
    for i in range(0, length):
        if i%2 == 1:
            sum += int(n[i])
        else:
            if int(n[i]) != 0:
                product *= int(n[i])
                test += 1
    if test == 0:
        print('0 ')
    else:
        print(str(product) + ' ', end=(''))
    print(str(sum))
    t-=1