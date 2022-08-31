import math
p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
for i in range(0, 1564748):
    arrin = str(input())
    arrin = arrin.split()
    if int(arrin[0]) == 0:
        break
    else:
        arrx = arrin[1]
        j = len(arrx)-1
        while j >= 0:
            x = 0
            while arrx[j] != p[x]:
                x+=1
            print(p[(x + int(arrin[0]))%28], end=(''))
            j-=1
        print('')
