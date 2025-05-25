
# 2292: 벌집

N = int(input())

count = 1
total = 1

while N > total:
	total += count*6
	count += 1

print(count)