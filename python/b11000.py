import sys
import heapq

# 11000: 강의실 배정

n = int(sys.stdin.readline())

classes = list()
for i in range(n):
	s, t = map(int, sys.stdin.readline().split())
	classes.append([s, t])
# print(f"input: {classes}")
classes.sort()
# print(f"after: {classes}")

room = list()
heapq.heappush(room, classes[0][1])
for i in range(1, n):
	if room[0] <= classes[i][0]:
		# print(f"pop: {room[0]} <= {classes[i][0]}")
		heapq.heappop(room)
		# print(f"pop: {room}")
	heapq.heappush(room, classes[i][1])
	# print(f"room #{i}: {room}")

print(len(room))