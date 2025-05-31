
# 5622: 다이얼

S = input()

total = 0
for s in S:
	if s == 'Z':
		time = 10
	elif s >= 'S':
		time = (ord(s) - ord('A') - 1) / 3 + 3
	else:
		time = (ord(s) - ord('A')) / 3 + 3
	total += int(time)
	print(f"{s}: {int(time)}")
print(total)