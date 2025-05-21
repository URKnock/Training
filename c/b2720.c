#include <stdio.h>

// 2720: 세탁소 사장 동혁

int main(void) {
	int T, C, m, i, j;
	int n[4] = {25, 10, 5, 1};

	scanf("%d", &T)

	for (i = 0; i < T; i++) {
		scanf("%d", &C);
		for (j = 0; j < 4; j++) {
			m = C / n[j]
			C = C - (m * n[j])
			printf("%d ", m);
		}
		printf("\n");
	}
}