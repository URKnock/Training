
# 1978: 소수 찾기

N = int(input())
number = input().split(" ")

count = 0
for num in number:
	n = int(num)
	if n < 2:
		isprime = False
	else:
		isprime = True
		for i in range(2, n):
			if n % i == 0:
				isprime = False
				break
	if isprime:
		count += 1

print(count)