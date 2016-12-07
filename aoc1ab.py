def solve():
	direction = 0  # north = 0, east = 1, south = 2, west = 3
	x = 0
	y = 0
	moves = [x for x in input().split(',')]
	visited = []
	for elem in moves:
		elem = elem.strip()
		turn = elem[0]
		length = int(elem[1:])
		if (turn == "R"):
			direction = abs((direction + 1) % 4)
		elif (turn == "L"):
			direction = abs((direction - 1) % 4)
		if (direction == 0):
			for _ in range(length):
				y += 1
				visit = (x, y)
				if visit in visited:
					return (abs(x) + abs(y))
				else:
					visited.append(visit)
		elif (direction == 1):
			for _ in range(length):
				x += 1
				visit = (x, y)
				if visit in visited:
					return (abs(x) + abs(y))
				else:
					visited.append(visit)
		elif (direction == 2):
			for _ in range(length):
				y -= 1
				visit = (x, y)
				if visit in visited:
					return (abs(x) + abs(y))
				else:
					visited.append(visit)
		else:
			for _ in range(length):
				x -= 1
				visit = (x, y)
				if visit in visited:
					return (abs(x) + abs(y))
				else:
					visited.append(visit)

print (solve())