import sys

# 28279: 덱 2

class deque:
	def __init__(self, n):
		self.head = 0
		self.tail = 0
		self.data = [0 for i in range(n)]
		self.max = n
		self.len = 0

	def isempty(self):
		if self.len == 0:
			return 1
		return 0

	def addhead(self, x):
		self.data[self.head] = x
		self.head = (self.head - 1) % self.max
		self.len += 1

	def addback(self, x):
		self.tail = (self.tail + 1) % self.max
		self.data[self.tail] = x
		self.len += 1

	def pophead(self):
		if self.len == 0:
			return -1
		self.head = (self.head + 1) % self.max
		self.len -= 1
		return self.data[self.head]

	def popback(self):
		if self.len == 0:
			return -1
		temp = self.data[self.tail]
		self.tail = (self.tail - 1) % self.max
		self.len -= 1
		return temp

	def gethead(self):
		if self.len == 0:
			return -1
		return self.data[(self.head + 1) % self.max]

	def getback(self):
		if self.len == 0:
			return -1
		return self.data[self.tail]


n = int(sys.stdin.readline())
data = deque(n)

for i in range(n):
	line = sys.stdin.readline().rstrip().split()
	if len(line) > 1:
		cmd, x = map(int, line)
	else:
		cmd = int(line[0])
	if cmd == 1:
		data.addhead(x)
	elif cmd == 2:
		data.addback(x)
	elif cmd == 3:
		print(data.pophead())
	elif cmd == 4:
		print(data.popback())
	elif cmd == 5:
		print(data.len)
	elif cmd == 6:
		print(data.isempty())
	elif cmd == 7:
		print(data.gethead())
	elif cmd == 8:
		print(data.getback())