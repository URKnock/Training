#include <stdio.h>

// 2903: 중앙 이동 알고리즘

int main(void) {
	int N, i;
	int pow = 0;
	int dot = 2;

	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		if (i == 0) {
			pow = 1;
		} else {
			pow *= 2;
		}
		dot += pow;
	}
	printf("%d", dot*dot);
}