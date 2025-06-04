
# 9461: 파도반 수열

def solution(n):
	for i in range(3, n):
		dp[i] = dp[i-2] + dp[i-3]

T = int(input())

for i in range(T):
	n = int(input())
	dp = list()
	for j in range(3):
		dp.append(1)
	for j in range(3, n):
		dp.append(0)
	solution(n)
	print(dp[n-1])