
# 2501: 약수 구하기

inputs = input().split(" ")
N = int(inputs[0])
K = int(inputs[1])

count = 0
result = 0
for i in range(1, N+1):
	if N % i == 0:
		count += 1
		if count == K:
			result = i
			break

print(result)