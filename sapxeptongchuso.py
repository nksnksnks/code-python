import math
def tich(x):
    summ = 1
    for i in range(0, len(x)):
            summ *= float(x[i])
    return summ
t = int(input())
while t > 0:
    n = int(input())
    arrin = str(input())
    arrin = arrin.split()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if tich(arrin[i]) > tich(arrin[j]):
                swap = arrin[i]
                arrin[i] = arrin[j]
                arrin[j] = swap
            if tich(arrin[i]) == tich(arrin[j]) and float(arrin[i]) > float(arrin[j]):
                swapp = arrin[i]
                arrin[i] = arrin[j]
                arrin[j] = swapp
    for i in range(0, n):
        print(arrin[i], end=(' '))
    print('')
    t -= 1
    