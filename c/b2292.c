#include <stdio.h>

// 2292: 벌집

int main(void) {
	int N;
	int count = 1;
	int total = 1;

	scanf("%d", &N);

	while (N > total) {
		total += count * 6;
		count++;
	}

	printf("%d", count);
	return 0;
}