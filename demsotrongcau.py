t = int(input())
while t>0:
    s = input()
    s_test = input()
    length = len(s)
    length_test = len(s_test)
    ds = 0
    i=length_test
    while i<length+1:
        if int(s[(i-length_test):i]) == int(s_test):
            ds += 1
            i+=length_test
        else:
            i+=1
    print(ds)
    t-=1