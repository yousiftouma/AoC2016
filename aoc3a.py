
def isOk(seq):
	a = seq[0]
	b = seq[1]
	c = seq[2]
	
	if (a+b > c):
		if (a+c > b):
			if (b+c > a):
				return True
	return False

res = 0
while True:
	values = [int(x) for x in input().split()]
	if isOk(values):
		res += 1
	print ("res is currently " + str(res))
		