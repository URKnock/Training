
# 7682: 틱택토
# 정답: https://mimsdatastudy.tistory.com/75

data = input()
while data != "end":

	xcnt = 0
	ocnt = 0
	xbcnt = 0
	obcnt = 0
	isvalid = True

	for d in data:
		if d == "X":
			xcnt += 1
		elif d == "O":
			ocnt += 1
	if xcnt == ocnt or xcnt-1 == ocnt:
		pass
	else:
		isvalid = False
	
	if isvalid:
		for i in range(3):
			w = '.'
			h = '.'
			for j in range(3):
				if w == '.':
					w = data[i*3+j]
				elif w != data[i*3+j]:
					w = 'F'
				if h == '.':
					h = data[i+j*3]
				elif h != data[i+j*3]:
					h = 'F'
			if w == 'X':
				xbcnt += 1
			elif w == 'O':
				obcnt += 1
			if h == 'X':
				xbcnt += 1
			elif h == 'O':
				obcnt += 1
		if (data[0] == data[4] and data[4] == data[8]) or (data[2] == data[4] and data[4] == data[6]):
			if data[4] == 'X':
				xbcnt += 1
			elif data[4] == 'O':
				obcnt += 1

	if isvalid:
		if xbcnt > 0:
			if obcnt > 0:
				isvalid = False
			if xcnt == ocnt:
				isvalid = False
		elif xbcnt == 0:
			if obcnt > 0:
				if xcnt > ocnt:
					isvalid = False
			elif obcnt == 0:
				if xcnt + ocnt != 9:
					isvalid = False

	if isvalid:
		print("valid\n")
	else:
		print("invalid\n")

	data = input()