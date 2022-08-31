import array as arr
n= int(input())
arrin = input()
arrin = arrin.split()
x = 1
n1 = n
while x > 0:
    check = 0
    for i in range(1, n1):
        if((int(arrin[i]) + int(arrin[i-1]))%2 == 0):
            popped = arrin.pop(i-1)
            popped = arrin.pop(i)
            check = 1
            break
    if(check == 0):
        x=0
    else:
        n1-=2
        if(n1 == 0):
            break
print(n1)

