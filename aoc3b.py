
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
	triangles = []
	triangle1 = []
	triangle2 = []
	triangle3 = []
	for i in range (3):
		values = [int(x) for x in input().split()]
		triangle1.append(values[0])
		triangle2.append(values[1])
		triangle3.append(values[2])
	triangles.append(triangle1)
	triangles.append(triangle2)
	triangles.append(triangle3)
	for triangle in triangles:
		if isOk(triangle):
			res += 1
	print ("res is currently " + str(res))
		