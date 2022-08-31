import math

a = int(input())
arr = []
for i in range(0, a):
        arr.append(list(map(int, input().split())))
top = 0
bot = 0
j1 = a
for i in range(0, a-1):
    j1-=1
    for z in range(0, j1):
        top = top + int(arr[i][z])
j2 = a
for i in range(1, a):
    j2-=1
    j = j2
    for z in range(j, a):
        bot = bot + int(arr[i][z])
k = int(input())
ds = int(top) - int(bot)
ds=int(math.sqrt(ds*ds))
if ds > k:
    print("NO")
else:
    print("YES")
print(ds)