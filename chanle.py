def testcl():
    x = input()
    length = len(x)
    sum = int(x[0])
    for i in range(0, length-1):
        sum = sum + int(x[i+1])
        if int(x[i]) - int(x[i+1]) != 2 and int(x[i+1]) - int(x[i]) != 2:
            return False
    if sum%10==0:
        return True
    else:
        return False
t = int(input())
while t > 0:
    if testcl() == True:
        print('YES')
    else:
        print('NO')
    t-=1