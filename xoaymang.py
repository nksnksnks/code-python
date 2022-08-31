import array as arr
t = int(input())
while(t>0):
    n,k = map(int,input().split())
    arrin = input()
    arrin = arrin.split()
    for i in range(k, n):
        print(arrin[i], end=(' '))
    for i in range(0, k):
        print(arrin[i], end=(' '))
    print('')
    t-=1