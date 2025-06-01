
# 5086: 배수와 약수

while True:
	inputs = input().split(" ")
	a = int(inputs[0])
	b = int(inputs[1])
	if a == 0 and b == 0:
		break
	if b % a == 0:
		print("factor")
	elif a % b == 0:
		print("multiple")
	else:
		print("neither")