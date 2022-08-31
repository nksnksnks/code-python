
t = int(input())
while t > 0:
	n = int(input())
	n1=str(n)
	length = int(len(str(n)))
	if length == 1:
		print(n)
	else:
		j=length-1
		for i in range(1, length):
			if int(n1[j]) >= 5:
				n=n+(10-int(n1[j]))*(10**(length-j-1))
			else:
				n=n-int(n1[j])*(10**(length-j-1))
			j=j-1
			n1=str(n)
		print(n1)
	t = t - 1