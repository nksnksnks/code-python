n = input()
length = len(n)
for i in range(0, length):
    if n[i] != ' ':
        print(n[i], end='')
    else:
        print('')