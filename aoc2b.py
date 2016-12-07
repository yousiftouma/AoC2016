col1 = [False, False, 5, False, False]
col2 = [False, 2, 6, "A", False]
col3 = [1,3,7,"B","D"]
col4 = [False, 4, 8, "C", False]
col5 = [False, False, 9, False, False]
keypad = [col1,col2,col3,col4,col5]

moves = []
for i in range(5):
	moves.append(input())

ans = "";

x = 0
y = 2

move = {"U" : (0, -1), "L" : (-1,0), "R" : (1,0), "D" : (0,1)}

for mov in moves:
	for m in mov:
		a = x
		b = y
		a += move[m][0]
		b += move[m][1]
		if (a <= 4 and a >= 0 and b <=4 and b >= 0 and keypad[a][b]):
			x += move[m][0]
			y += move[m][1]
	ans += str(keypad[x][y])

print(ans)
