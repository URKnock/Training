
# 2745: 진법 변환

inputs = input().split(" ")
N = inputs[0][::-1]
B = inputs[1]

result = 0

for i in range(len(N)):
	if N[i].isdigit():
		data = int(N[i])
	else:
		data = (ord(N[i]) - ord('A') + 10)
	for j in range(i):
		data *= int(B)
	result += data

print(result)