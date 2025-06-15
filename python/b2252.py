import sys
from collections import deque

# 2252: 줄 세우기

n, m = map(int, sys.stdin.readline().split())

graph = list()
indegree = list()
for i in range(n+1):
	graph.append(list())
	indegree.append(0)

for i in range(m):
	na, nb = map(int, sys.stdin.readline().split())
	graph[na].append(nb)
	indegree[nb] += 1

def topology_sort():
	result = list()
	queue = deque()
	for i in range(1, n+1):
		if indegree[i] == 0:
			queue.append(i)
	while queue:
		q = queue.popleft()
		result.append(q)
		for g in graph[q]:
			indegree[g] -= 1
			if indegree[g] == 0:
				queue.append(g)
	return result

data = topology_sort()
print(" ".join(map(str, data)))