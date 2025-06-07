
# 2231: 분해합

N = int(input())

result = 0
for i in range(N+1):
	num = i
	count = num
	while num > 0:
		count += num % 10
		num = int(num / 10)
	if count == N:
		result = i
		break

print(result)