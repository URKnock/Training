import sys

# 1620: 나는야 포켓몬 마스터 이다솜

n, m = map(int, sys.stdin.readline().rstrip().split())

name = {}
index = {}

for i in range(n):
	data = sys.stdin.readline().rstrip()
	name[data] = i+1
	index[str(i+1)] = data

result = ""
for i in range(m):
	quest = sys.stdin.readline().rstrip()
	if quest.isdigit():
		result += f"{index[quest]}\n"
	else:
		result += f"{name[quest]}\n"

print(result)