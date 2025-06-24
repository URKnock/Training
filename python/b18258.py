import sys

# 18258: 큐 2

queue = list()
qsize = 0
qsrc = 0
qdst = 0

n = int(sys.stdin.readline())

for i in range(n):
	inputs = sys.stdin.readline()[:-1].split(" ")
	if len(inputs) > 1:
		cmd = inputs[0]
		data = inputs[1]
	else:
		cmd = inputs[0]
	if cmd == "push":
		queue.append(data)
		qdst += 1
		qsize += 1
	elif cmd == "pop":
		if qsize == 0:
			print("-1")
		else:
			print(queue[qsrc])
			qsize -= 1
			qsrc += 1
	elif cmd == "size":
		print(qsize)
	elif cmd == "empty":
		if qsize == 0:
			print("1")
		else:
			print("0")
	elif cmd == "front":
		if qsize == 0:
			print("-1")
		else:
			print(queue[qsrc])
	elif cmd == "back":
		if qsize == 0:
			print("-1")
		else:
			print(queue[qdst-1])
	elif cmd == "print":
		print(f"qsrc: {qsrc}")
		print(f"qdst: {qdst}")
		print(f"qsize: {qsize}")
		for i in range(qsrc, qdst):
			print(queue[i])
