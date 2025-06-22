import sys

# 2566: 최댓값

def solution(line):
	ml = 0
	yl = 0
	for j in range(9):
		if ml < line[j]:
			ml = line[j]
			yl = j
	return ml, yl

m = 0
mx, my = 0, 0
for i in range(9):
	line = list(map(int, sys.stdin.readline().split()))
	lm, ly = solution(line)
	if lm > m:
		m = lm
		mx = i
		my = ly

print(m)
print(f"{mx+1} {my+1}")