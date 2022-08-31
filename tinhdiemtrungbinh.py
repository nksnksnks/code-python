import math
n = int(input())
a = input()
a = a.split()
for i in range(0, n-1):
    for j in range(i+1, n):
        if(float(a[i]) > float(a[j])):
            swap = a[i]
            a[i] = a[j]
            a[j] = swap
sum = 0
dem = n
for i in range(0, n):
    if(float(a[0]) != float(a[i]) and float(a[n-1]) != float(a[i])):
        sum += float(a[i])
    else:
        dem-=1
kq = sum/dem
print("{:.2f}".format(float(kq)))
    
