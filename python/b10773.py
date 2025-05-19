
# 10773: 제로

stack = list()
stack_size = -1
stack_max = 100000

def isfull():
	global stack_size
	global stack_max
	if stack_size == stack_max:
		return True
	return False

def isempty():
	global stack_size
	if stack_size == -1:
		return True
	return False

def push(n):
	global stack_size
	if isfull():
		return
	stack_size += 1
	stack.append(n)

def pop():
	global stack_size
	if isempty():
		return -1
	stack_size -= 1
	return stack.pop()

K = int(input())

for i in range(K):
	n = int(input())
	if n == 0:
		pop()
	else:
		push(n)

result = 0
for i in range(stack_size+1):
	result += pop()
print(result)