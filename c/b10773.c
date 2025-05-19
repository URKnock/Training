#include <stdio.h>
#define STACK_MAX 100000

// 10773: 제로

static int stack[STACK_MAX] = {0,};
static int stack_size = -1;

int isfull(void) {
	if (stack_size == STACK_MAX) {
		return 1;
	}
	return 0;
}

int isempty(void) {
	if (stack_size == -1) {
		return 1;
	}
	return 0;
}

void push(int n) {
	if (isfull() == 1) {
		return;
	}
	stack_size += 1;
	stack[stack_size] = n;
}

int pop() {
	int n;
	if (isempty() == 1) {
		return 0;
	}
	n = stack[stack_size];
	stack_size -= 1;
	return n;
}

int main(void) {
	int K, i, n;
	int result = 0;

	scanf("%d", &K);
	for (i = 0; i < K; i++) {
		scanf("%d", &n);
		if (n == 0) {
			pop();
		} else {
			push(n);
		}
	}

	n = stack_size + 1;
	for (i = 0; i < n; i++) {
		result += pop();
	}

	printf("%d", result);
	return 0;
}