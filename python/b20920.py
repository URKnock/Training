import sys

# 20920: 영단어 암기는 괴로워

words = {}

n, m = map(int, sys.stdin.readline().split())

for i in range(n):
	word = sys.stdin.readline().rstrip()
	if len(word) < m:
		continue
	if words.get(word) is None:
		words[word] = 1
	else:
		words[word] += 1

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# print("---")
for word in words:
	print(word[0])