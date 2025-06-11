import sys

# 2839: 설탕 배달

n = int(sys.stdin.readline())

find = False
mins = 5000
max5 = int(n/5)+1
max3 = int(n/3)+1

for x in range(max5):
	for y in range(max3):
		if x*5+y*3 == n:
			find = True
			if mins > x+y:
				mins = x+y
if find:
	print(mins)
else:
	print("-1")