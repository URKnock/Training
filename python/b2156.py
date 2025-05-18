
# 2156: 포도주 시식

def solution(n):
	dp[0] = w[0]
	if n > 1:
		dp[1] = w[0] + w[1]
	if n > 2:
		dp[2] = max(w[1]+w[2], w[0]+w[2], dp[1])
	for i in range(3, n):
		dp[i] = max(dp[i-1], dp[i-3]+w[i-1]+w[i], dp[i-2]+w[i])

n = int(input())

dp = list()
for i in range(n):
	dp.append(0)

w = list()
for i in range(n):
	wines = int(input())
	w.append(wines)

solution(n)
print(dp[n-1])