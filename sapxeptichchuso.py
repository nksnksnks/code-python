import math
def sum(x):
    summ = 0
    for i in range(0, len(x)):
        summ += int(x[i])
    return summ
t = int(input())
while t > 0:
    n =int(input())
    arrin = str(input())
    arrin = arrin.split()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if sum(arrin[i]) > sum(arrin[j]):
                swap = arrin[i]
                arrin[i] = arrin[j]
                arrin[j] = swap
            if sum(arrin[i]) == sum(arrin[j]) and float(arrin[i]) > float(arrin[j]):
                swap = arrin[i]
                arrin[i] = arrin[j]
                arrin[j] = swap
    for i in range(0, n):
        print(arrin[i], end=(' '))
    print('')
    t -= 1
    