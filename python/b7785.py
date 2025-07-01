import sys

# 7785: 회사에 있는 사람

n = int(sys.stdin.readline())

data = {}

for i in range(n):
	person, state = sys.stdin.readline().rstrip().split()
	if state == "enter":
		data[person] = 1
	else:
		data[person] = 0

result = []
for k in data.keys():
	if data[k] != 0:
		result.append(k)

result = sorted(result, reverse=True)
for r in result:
	print(r)