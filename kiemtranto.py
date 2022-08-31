import math
import array as arr
def nto(n):
    if n < 2 or n == 4:
        return 0
    if n == 2 or n == 3:
        return 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1
a, b = map(int, input().split())
arrin = []
for i in range(a):
        arrin.append(list(map(int, input().split())))
for i in range(0, a):
    for j in range(0, b):
        if nto(arrin[i][j]) == 1:
            arrin[i][j] = 1
        else:
            arrin[i][j] = 0
for i in range(0, a):
    for j in range(0, b):
        print(arrin[i][j], end = (' '))
    print('')
