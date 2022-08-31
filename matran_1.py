import math

a = int(input())
arr = []
for i in range(0, a):
        arr.append(list(map(int, input().split())))
top = 0
bot = 0
for i in range(0, a):
    for j in range(0, a):
        if int(j) > int(i):
            top = top + int(arr[i][j])
        if int(j) < int(i):
            bot = bot + int(arr[i][j])
k = int(input())
z = int(top) - int(bot)
if int(math.sqrt(z*z)) > k:
    print("NO")
else:
    print("YES")
print(int(math.sqrt(z*z)))
