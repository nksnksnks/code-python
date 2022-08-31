n = input()
length = len(n)
first = length%3
if first == 0:
    first = 3
for i in range(0, first):
    print(n[i], end=(''))
for i in range(first, length, 3):
    print(',', end=(''))
    print(n[i] + n[i+1] + n[i+2], end=(''))