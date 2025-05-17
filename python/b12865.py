
# 12865: 평범한 배낭

def solution(N, K):
	for i in range(1, K+1):
		for j in range(1, N+1):
			if w[j] > i:
				dp[j][i] = dp[j-1][i]
			else:
				dp[j][i] = max(dp[j-1][i-w[j]] + v[j], dp[j-1][i])

inputs = input().split(" ")
N = int(inputs[0])
K = int(inputs[1])

dp = list()
for i in range(N+1):
	d = list()
	for j in range(K+1):
		d.append(0)
	dp.append(d)

w = list()
v = list()
w.append(0)
v.append(0)

for i in range(N):
	bags = input().split(" ")
	w.append(int(bags[0]))
	v.append(int(bags[1]))

solution(N, K)
print(dp[N][K])