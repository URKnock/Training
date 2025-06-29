import sys

# 11866: 요세푸스 문제 0

class queue:
	def __init__(self, n):
		self.head = 0
		self.tail = 0
		self.data = [0 for i in range(n+1)]
		self.max = n+1

	def isempty(self):
		if self.head == self.tail:
			return True
		return False

	def isfull(self):
		if ((self.tail + 1) % self.max) == self.head:
			return True
		return False

	def enqueue(self, d):
		if self.isfull():
			return
		self.tail = (self.tail + 1) % self.max
		self.data[self.tail] = d
		return

	def dequeue(self):
		if self.isempty():
			return
		self.head = (self.head + 1) % self.max
		return self.data[self.head]

n, k = map(int, sys.stdin.readline().split())

data = queue(n)
result = list()

for i in range(n):
	data.enqueue(i+1)

while not data.isempty():
	for i in range(k-1):
		d = data.dequeue()
		data.enqueue(d)
	d = data.dequeue()
	result.append(str(d))

print(f"<{', '.join(result)}>")