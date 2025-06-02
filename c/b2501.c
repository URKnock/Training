#include <stdio.h>

// 2501: 약수 구하기

int main(void) {
	int N, K, i;
	int count = 0;
	int result = 0;

	scanf("%d %d", &N, &K);

	for (i = 1; i <= N; i++) {
		if (N % i == 0) {
			count++;
			if (count == K) {
				result = i;
				break;
			}
		}
	}

	printf("%d\n", result);
	return 0;
}