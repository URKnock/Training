#include <stdio.h>

// 1193: 분수찾기

int main(void) {
	int X, temp, i;
	int L = 1;
	int R = 1;
	int down = 1;
	int count = 1;

	scanf("%d", &X);

	while (1) {
		temp = L + 4*count;
		if (X < temp) {
			R = count;
			count = L;
			L = R;
			if (count > 1) {
				down = 0;
			}
			break;
		}
		L = temp;
		count += 1;
	}

	for (i = 0; i < X-count; i++) {
		if (L == 1) {
			if (R % 2 == 1) {
				R++;
			} else {
				down = 1;
				R--;
				L++;
			}
		} else {
			if (R == 1) {
				if (L % 2 == 0) {
					L++;
				} else {
					down = 0;
					L--;
					R++;
				}
			} else {
				if (down == 1) {
					R--;
					L++;
				} else {
					L--;
					R++;
				}
			}
		}
	}

	printf("%d/%d", L, R);
	return 0;
}