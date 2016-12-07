keypad = [[0 for x in range(3)] for y in range(3)]
k = 1
for i in range(3):
	for j in range(3):
		keypad[j][i] = k
		k += 1

print(keypad)
print(keypad[1][1])
print(keypad[0][2])
print(keypad[2][1])

moves = []
for i in range(5):
	moves.append(input())

ans = "";

x = 1
y = 1

move = {"U" : (0, -1), "L" : (-1,0), "R" : (1,0), "D" : (0,1)}

for mov in moves:
	for m in mov:
		a = x
		b = y
		a += move[m][0]
		b += move[m][1]
		if (a <= 2 and a >= 0 and b <=2 and b >= 0):
			x += move[m][0]
			y += move[m][1]
	ans += str(keypad[x][y])

print(ans)