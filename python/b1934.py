import sys

# 1934: 최소공배수

def swap(a, b):
	if a < b:
		temp = a
		a = b
		b = temp
	return a, b

def solution(a, b):
	while b != 0:
		last = a % b
		a = b
		b = last
	return a

t = int(sys.stdin.readline())

for j in range(t):
	a, b = map(int, sys.stdin.readline().split())
	a, b = swap(a, b)
	print(a * b // solution(a, b))