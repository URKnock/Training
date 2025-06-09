import sys

# 2108: 통계학

# result1 - 산술평균
# result2 - 중앙값
# result3 - 최빈값
# result4 - 범위

N = int(input())

temp = dict()
data = list()
for i in range(N):
	d = int(sys.stdin.readline())
	data.append(d)

result1 = 0
for d in data:
	result1 += d
	if temp.get(d) is None:
		temp[d] = 1
	else:
		temp[d] += 1

if result1 > 0:
	result1 = int(result1/N + 0.5)
else:
	result1 = int(result1/N - 0.5)

data = sorted(data)
result2 = data[int(N/2)]

val = sorted(temp, key=lambda x: temp[x], reverse=True)
cnt = temp.get(val[0])
if len(val) > 1 and cnt == temp.get(val[1]):
	same = list()
	for i in range(len(val)):
		if cnt == temp.get(val[i]):
			same.append(val[i])
		else:
			break
	val = sorted(same)
	result3 = val[1]
else:
	result3 = val[0]

result4 = data[-1] - data[0]
if result4 < 0:
	result4 = -result4

print(result1)
print(result2)
print(result3)
print(result4)