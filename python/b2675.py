
# 2675: 문자열 반복

T = input()
for t in range(int(T)):
	result = ""
	tc = input().split(' ')
	for s in tc[-1]:
		for r in range(int(tc[0])):
			result += s
	print(result)