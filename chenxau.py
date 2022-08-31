a = input()
a = a.split()
b = str(input())
vt = int(input())
vt -= 1
test = 0
for i in range(0, len(a)):
    if i == vt:
        print(b, end=(''))
        test = 1
        print(a[i], end =(' '))
    if i+1 == vt:
        print(a[i], end =(''))
    if i+1 != vt and i!=vt:
        print(a[i], end =(' '))
if test == 0:
    print(b, end=(''))