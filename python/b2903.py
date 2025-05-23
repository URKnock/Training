
# 2903: 중앙 이동 알고리즘

N = int(input())

dot = 2
for i in range(N):
	dot += pow(2, i)
print(dot * dot)