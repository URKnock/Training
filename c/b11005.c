#include <stdio.h>
#include <string.h>

// 11005: 진법 변환

int main(void) {
	int B, data, i, j;
	long long N;
	char result[36];

	scanf("%lld %d", &N, &B);

	i = 0;
	while (N > 0) {
		data = N % B;
		if (data > 9) {
			data += 'A' - 10;
		} else {
			data += '0';
		}
		result[i++] = data;
		N /= B;
	}

	for (j = i-1; j >= 0; j--) {
		printf("%c", result[j]);
	}
}