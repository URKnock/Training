
# 1193: 분수찾기

X = int(input())

L = 1
R = 1
down = True

count = 1
while True:
	temp = L + 4*count
	if X < temp:
		R = count
		count = L
		L = R
		if count > 1:
			down = False
		break
	L = temp
	count += 1

for i in range(X-count):
	if L == 1:
		if R % 2 == 1:
			R += 1
		else:
			down = True
			R -= 1
			L += 1
	elif R == 1:
		if L % 2 == 0:
			L += 1
		else:
			down = False
			L -= 1
			R += 1
	else:
		if down:
			R -= 1
			L += 1
		else:
			L -= 1
			R += 1

print(f"{L}/{R}")