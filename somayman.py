t = int(input())
while t>0:
    n = str(input())
    s = len(n)
    sum = 0
    for i in range(0, s):
        if int(n[i]) != 4 and int(n[i]) != 7:
            print("NO")
            break
        sum += 1
    if sum == len(n):
        print("YES")
    t-=1
    