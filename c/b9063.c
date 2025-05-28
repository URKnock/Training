#include <stdio.h>

// 9063: 대지

#define min(x, y) x < y ? x : y
#define max(x, y) x > y ? x : y
#define abs(x) x < 0 ? -x : x

int main(void) {
	int N, x, y, i;
	int x_min = 10000, x_max = -10000;
	int y_min = 10000, y_max = -10000;
	long long result;

	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%d %d", &x, &y);
		x_min = min(x_min, x);
		x_max = max(x_max, x);
		y_min = min(y_min, y);
		y_max = max(y_max, y);
	}

	if (N < 2) {
		result = 0;
	} else {
		x = abs(x_max - x_min);
		y = abs(y_max - y_min);
		result = x * y;
	}
	printf("%lld", result);
	return 0;
}