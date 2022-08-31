n = int(input())
a = input()
a = a.split()
b = []
test = 0
for i in range(1,30002): 
    if a.count(str(i)) == 0:
        print(i)
        break
        
        
        

    