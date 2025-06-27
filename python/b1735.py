import sys

# 1735: 분수 합

def swap(a, b):
	if a < b:
		temp = a
		a = b
		b = temp
	return a, b

def minnum(a, b):
	swap(a, b)
	while b != 0:
		last = a % b
		a = b
		b = last
	return a

def maxnum(a, b):
	return a * b // minnum(a, b)

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

deno = maxnum(b, d)
a = deno // b * a
c = deno // d * c

nume = a + c
divisor = minnum(nume, deno)
nume = nume // divisor
deno = deno // divisor

print(f"{nume} {deno}")