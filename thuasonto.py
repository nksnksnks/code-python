t = int(input())
while t > 0:
    n = int(input())
    print('1', end = (''))
    shared = 2
    while n > 1:
        dem = 0
        while n % shared ==0:
            n = n/shared
            dem +=1
        if(dem > 0):
            print(' * '+ str(shared) + '^' + str(dem), end=(''))
        shared += 1
    print('')
    t-=1