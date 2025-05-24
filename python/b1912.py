
# 1912: 연속합

def solution(n):
	dp[0] = d[0]
	for i in range(1, n):
		dp[i] = max(dp[i-1]+d[i], d[i])

n = int(input())
d = list(map(int, input().split(" ")))

dp = list()
for i in range(n):
	dp.append(0)

solution(n)
print(dp)
print(max(dp))