import sys

# 26069: 붙임성 좋은 총총이

n = int(sys.stdin.readline())

dance = set()
dance.add("ChongChong")

for i in range(n):
	meet = sys.stdin.readline().replace("\n", "").split(" ")
	indance = False
	for m in meet:
		if m in dance:
			indance = True
			break
	if indance:
		for m in meet:
			dance.add(m)

print(len(dance))