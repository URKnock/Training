#include <stdio.h>
#include <stdlib.h>

// 9461: 파도반 수열

void solution(int* dp, int n) {
	int i;
	for (i = 3; i < n; i++) {
		dp[i] = dp[i-2] + dp[i-3];
	}
}

int main(void) {
	int t, n, i, j;
	int *dp;

	scanf("%d", &t);

	for (i = 0; i < t; i++) {
		scanf("%d", &n);
		dp = (int*) malloc(sizeof(int)*n);
		for (j = 0; j < 3; j++) {
			dp[j] = 1;
		}
		for (j = 3; j < n; j++) {
			dp[j] = 0;
		}
		solution(dp, n);
		printf("%d\n", dp[n-1]);
	}

	return 0;
}