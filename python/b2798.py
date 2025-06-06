
# 2798: 블랙잭

def abs(x):
	if x > 0:
		return x
	return -x

inputs = input().split(" ")
N = int(inputs[0])
M = int(inputs[1])

inputs = input().split(" ")
data = list(map(int, inputs))
data = sorted(data, reverse=True)
l = len(data)

result = M
diff = M

for i in range(l):
	for j in range(i+1, l):
		for k in range(j+1, l):
			total = data[i] + data[j] + data[k]
			if total <= M:
				tiff = abs(M-total)
				if diff > tiff:
					diff = tiff
					result = total

print(result)