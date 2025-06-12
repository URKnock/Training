import sys

# 1436: 영화감독 숌

n = int(sys.stdin.readline())

cnt = 0
for i in range(666, 2666800):
	if "666" in str(i):
		cnt += 1
		if cnt == n:
			print(i)
			break