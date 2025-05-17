#include <stdio.h>

// 12865: 진법 변환

int w[101] = {0,};
int v[101] = {0,};
int dp[101][101] = {0,};

int max(int a, int b) {
	if (a > b) {
		return a;
	}
	return b;
}

void solution(int N, int K) {
	int i, j;
	for (i = 1; i <= K; i++) {
		for (j = 1; j <= N; j++) {
			if (w[j] > i) {
				dp[j][i] = dp[j-1][i];
			} else {
				dp[j][i] = max(dp[j-1][i-w[j]]+v[j], dp[j-1][i]);
			}
		}
	}
}

int main(void) {
	int N, K, i, j;
	for (i = 0; i <= N; i++) {
		for (j = 0; j <= K; j++) {
			dp[i][j] = 0;
		}
	}
	scanf("%d %d", &N, &K);
	for (i = 0; i < N; i++) {
		scanf("%d %d", &w[i+1], &v[i+1]);
	}

	solution(N, K);
	printf("%d", dp[N][K]);

	return 0;
}