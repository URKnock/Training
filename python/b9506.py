
# 9506: 약수들의 합

n = int(input())
while n != -1:
	data = list()
	for i in range(1, n):
		if n % i == 0:
			data.append(i)
	total = 0
	for d in data:
		total += d
		if total > n:
			break
	if total == n:
		result = f"{n} = "
		for d in data:
			result += f"{d} + "
		print(result[:-3])
	else:
		print(f"{n} is NOT perfect.")
	n = int(input())