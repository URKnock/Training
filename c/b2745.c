#include <stdio.h>
#include <string.h>

// 2745: 진법 변환

int main(void) {
	char N[36];
	int B, i, j;
	long long data;
	long long result = 0;

	scanf("%s %d", N, &B);

	for (i = 0; i < strlen(N); i++) {
		if (N[i] >= 'A' && N[i] <= 'Z') {
			data = N[i] - 'A' + 10;
		} else {
			data = N[i] - '0';
		}
		for (j = 0; j < strlen(N)-i-1; j++) {
			data *= B;
		}
		result += data;
	}
	printf("%lld", result);
}