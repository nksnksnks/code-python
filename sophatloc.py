t = int(input())
while t > 0:
    x = input()
    if int(x[length-1]) == 6 and int(x[length-2]) == 6:
        print("YES")
    else:
        print("NO")
    t-=1