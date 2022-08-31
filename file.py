file = open("test.txt", "r+")
s = file.read()
length = len(s)
if s[length-3:length] == '.py':
    print ("yes")
else:
    print("no")