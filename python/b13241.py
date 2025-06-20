import sys

# 13241: 최소공배수

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

a, b = map(int, sys.stdin.readline().split())
a, b = swap(a, b)
print(a * b // solution(a, b))