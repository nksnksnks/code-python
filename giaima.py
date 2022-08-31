t = int(input())
while t > 0:
    n = input()
    vt=0
    length = len(n)
    for i in range(1, length+1, 2):
        for j in range(0, int(n[i])):
            print(n[vt], end='')
        vt += 2
    t-=1
    print('')
