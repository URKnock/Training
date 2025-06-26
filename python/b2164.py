import sys

# 2164: 카드2

queue = list()
meta = {
	"src": 0,
	"dst": 0
}

def queue_push(data):
	queue.append(data)
	meta["dst"] += 1

def queue_pop():
	if meta["src"] == meta["dst"]:
		return -1
	idx = meta["src"]
	meta["src"] += 1
	return queue[idx]

def queue_print(idx=0):
	src = meta["src"]
	dst = meta["dst"]
	print(f"src: {src} / dst = {dst}")
	if idx == 0:
		result = "queue: "
	else:
		result = f"#{idx} queue: "
	for i in range(src, dst):
		result += f"{queue[i]} "
	print(result)

n = int(sys.stdin.readline())

for i in range(1, n+1):
	queue_push(i)
# queue_print()

i = 1
while(meta["src"] != meta["dst"]):
	data = queue_pop()
	if i % 2 == 0:
		queue_push(data)
	# queue_print(i)
	i += 1

print(data)
