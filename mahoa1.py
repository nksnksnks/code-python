t = int(input())
while t > 0:
    n = input()
    length = len(n)
    x = 1
    j1 = 0
    sum = 0
    step = 1
    i = 0
    while i < length:
        pawn = n[i]
        for j in range(i, length):
            if n[j] == pawn:
                sum += 1
                j1 = j+1
            else:
                break
        print(str(sum) + str(pawn), end=(''))
        sum = 0
        i = j1
    print('')
    t-=1