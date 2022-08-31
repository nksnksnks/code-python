import array as arr

n = int(input())
arrin = str(input())
arrin = arrin.split()
dem = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        if float(arrin[i]) > float(arrin[j]):
            dem +=1
print(dem)
#    a, b = map(int, input().split())