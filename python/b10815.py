import sys

# 10815: 숫자 카드

n = int(sys.stdin.readline())
have = list(map(int, sys.stdin.readline().split()))
have = sorted(have)

m = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

def find(have, n, d):
	src = 0
	dst = n-1
	while src <= dst:
		idx = int((src+dst)/2)
		if have[idx] == d:
			return True
		elif have[idx] > d:
			dst = idx-1
		else:
			src = idx+1
	return False

result = list()
for d in data:
	if find(have, n, d):
		result.append("1")
	else:
		result.append("0")

print(" ".join(result))