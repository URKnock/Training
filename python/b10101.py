import sys

# 10101: 삼각형 외우기

angle = list()

for i in range(3):
	a = int(sys.stdin.readline())
	angle.append(a)

angle.sort()

isEquilateral = True
total = 0
for a in angle:
	if a != 60:
		isEquilateral = False
	total += a

if isEquilateral:
	print("Equilateral")
else:
	if total != 180:
		print("Error")
	elif angle[0] == angle[1] or angle[1] == angle[2]:
		print("Isosceles")
	else:
		print("Scalene")