
# 25192: 인사성 밝은 곰곰이

N = int(input())

count = 0
data = set()

for i in range(N):
	say = input()
	if say == "ENTER":
		count += len(data)
		data = set()
	else:
		data.add(say)

count += len(data)
print(count)