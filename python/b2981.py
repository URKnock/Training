import math

# 2981: 검문

N = int(input())
num = list()
for i in range(N):
	n = int(input())
	num.append(n)
num.sort()

temp = num[1] - num[0]
for i in range(2, N):
	temp = math.gcd(num[i] - num[i-1], temp)

M = list()
for i in range(2, int(temp**0.5)+1):
	if temp % i == 0:
		M.append(i)
		if i != temp / i:
			M.append(int(temp / i))

M.append(temp)
M = list(set(M))
M.sort()

result = ""
for i in M:
	result += f"{i} "
result = result[:-1]

print(result)