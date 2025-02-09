
# 10809: 알파벳 찾기

alpha = []
for i in range(26):
	alpha.append(-1)

S = input()
for i in range(len(S)):
	diff = ord(S[i].lower()) - 97
	if alpha[diff] == -1:
		alpha[diff] = i

result = ""
for i in range(26):
	result += f"{alpha[i]} "

print(result)