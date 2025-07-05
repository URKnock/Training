import sys

# 1269: 대칭 차집합

acnt, bcnt = map(int, sys.stdin.readline().rstrip().split())

a = set(map(int, sys.stdin.readline().rstrip().split()))
b = set(map(int, sys.stdin.readline().rstrip().split()))

result = (a - b) | (b - a)
print(len(result))