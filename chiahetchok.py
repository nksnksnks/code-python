a,k,n = map(int,input().split())
test = 0
s = a % k
for i in range(k-s, n-a+1, k):
    if (a+i) % k == 0:
        test +=1
        print(str(i) , end = ' ')
if test == 0:
    print('-1')