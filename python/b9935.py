
# 9935: 문자열 폭발

S = input()
F = input()
s_size = len(S)
f_size = len(F)

stack = list()

for i in range(s_size):
	stack.append(S[i])
	if ''.join(stack[-f_size:]) == F:
		for j in range(f_size):
			stack.pop()

result = ''.join(stack)
if result == "":
	print("FRULA")
else:
	print(result)