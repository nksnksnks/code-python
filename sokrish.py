def giaithua(n):
    test = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            test *= i
    return test
t =int(input())
while t > 0:
    sum = 0
    n = input()
    for i in range(0, len(n)):
        sum += giaithua(int(n[i]))
    if sum == int(n):
        print("Yes")
    else:
        print("No")
    t-=1