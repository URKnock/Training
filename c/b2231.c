#include <stdio.h>

// 2231: 분해합

int main(void) {
	int N, i, num, count;
	int result = 0;

	scanf("%d", &N);

	for (i = 0; i <= N; i++) {
		num = i;
		count = num;
		while (num > 0) {
			count += num % 10;
			num /= 10;
		}
		if (count == N) {
			result = i;
			break;
		}
	}
	printf("%d\n", result);
	return 0;
}