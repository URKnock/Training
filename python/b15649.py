import sys

# 15649: N과 M (1)

n, m = map(int, sys.stdin.readline().split())

data = list()
visited = [False] * (n+1)

def dfs(data, visited):
	if len(data) == m:
		print(" ".join(map(str, data)))
		return
	for i in range(1, n+1):
		if visited[i]:
			continue
		visited[i] = True
		
		data.append(i)
		dfs(data, visited)

		data.pop()
		visited[i] = False

dfs(data, visited)