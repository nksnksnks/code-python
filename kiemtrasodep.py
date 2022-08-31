def testcl():
    n = input()
    length = len(n)
    for i in range(2, length):
        if n[i] != n[i-2]:
            return False
    return True
t = int(input())
while t>0:
    if testcl() == True:
        print("YES")
    else:
        print("NO")
    t-=1