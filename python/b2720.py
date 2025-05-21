
# 2720: 세탁소 사장 동혁

T = int(input())

for i in range(T):
	C = int(input())
	result = ""
	for n in [25, 10, 5, 1]:
		m = int(C / n)
		C = C - (m * n)
		result += f"{m} "
	print(result[:-1])
