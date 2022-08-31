import math

t = int(input())
while t > 0:
    n = int(input())
    arr = str(input())
    arr = arr.split()
    print('1', end=(' '))
    for i in range(1,n):
        test = 0
        for j in range(i, 0, -1):
            if(int(arr[i]) >= int(arr[j])):
                test += 1
            else:
                break
        print(str(test), end=(' '))
    print('')
    t-=1