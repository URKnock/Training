import sys

# 10816: 숫자 카드 2

n = int(sys.stdin.readline().rstrip())
ndata = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
mdata = list(map(int, sys.stdin.readline().rstrip().split()))

card = {}

for d in ndata:
	if d in card:
		card[d] += 1
	else:
		card[d] = 1

for d in mdata:
	if d in card:
		print(card[d], end=' ')
	else:
		print(0, end=' ')