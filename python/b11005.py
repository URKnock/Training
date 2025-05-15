
# 11005: 진법 변환 2

inputs = input().split(" ")
N = int(inputs[0])
B = int(inputs[1])

result = ""

while N > 0:
	data = N % B
	if data > 9:
		data = chr(data + ord('A') - 10)
	result += str(data)
	N = int(N / B)

print(result[::-1])