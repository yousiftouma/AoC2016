

def isOk(words, hsh):
	for c in hsh:
		if c not in words:
			return False
		val = words[c]
		del words[c]
		for elem, value in words.items():
			if value > val:
				return False
			elif value == val:
				if elem < c:
					return False
	return True

def decipher(values):
	

while True:
	words = {}
	values = input().split("-")
	id = -1
	hsh = ""
	for code in values:
		if not "[" in code:
			for chr in code:
				if chr not in words:
					words[chr] = 0
				else:
					words[chr] += 1
		else:
			id = int(code[0:code.find("[")])
			hsh = code[code.find("[")+1:-1]
	if isOk(words, hsh):
		decipher(values)
	