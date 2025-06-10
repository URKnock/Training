import sys

# 19532: 수학은 비대면강의입니다

n = list(map(int, sys.stdin.readline().split(" ")))

for x in range(-999, 1000):
	for y in range(-999, 1000):
		if x*n[0] + y*n[1] == n[2] and x*n[3] + y*n[4] == n[5]:
			print(f"{x} {y}")
			break