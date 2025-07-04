import sys

# 1764: 듣보잡

n, m = map(int, sys.stdin.readline().rstrip().split())

hear = {}
result = []

for i in range(n):
	data = sys.stdin.readline().rstrip()
	hear[data] = 1

for i in range(m):
	data = sys.stdin.readline().rstrip()
	if data in hear:
		result.append(data)

result = sorted(result)
print(len(result))
print("\n".join(result))