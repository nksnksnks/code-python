from tokenize import Double


t = int(input())

while t>0:
    n = int(input())
    if n%2 == 0:
        spawn = 2
    else:
        spawn = 1
    sum = 0
    for i in range(spawn, n+1, 2):
        sum = sum + (1/i)
    print("{:.6f}".format(sum))
    t-=1