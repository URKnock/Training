import sys

# 1316: 그룹 단어 체커

def solution(word):
	temp = list()
	for i in range(1, len(word)):
		if word[i-1] != word[i]:
			if word[i] in temp:
				return False
			temp.append(word[i-1])
	return True

n = int(sys.stdin.readline())

result = 0
for i in range(n):
	word = sys.stdin.readline()
	if solution(word):
		result += 1
print(result)