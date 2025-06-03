#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 9506: 약수들의 합

int main(void) {
	int n, i, idx, total;
	int *data;
	char *buf, *temp;

	scanf("%d", &n);

	while (n != -1) {
		data = (int*) malloc(sizeof(int)*n);
		idx = 0;
		for (i = 1; i < n; i++) {
			if (n % i == 0) {
				data[idx++] = i;
			}
		}
		total = 0;
		for (i = 0; i < idx; i++) {
			total += data[i];
			if (total > n) {
				break;
			}
		}
		if (total == n) {
			buf = (char*) malloc(sizeof(char)*(n+1)*4);
			temp = (char*) malloc(sizeof(char)*10);
			sprintf(buf, "%d = ", n);
			for (i = 0; i < idx; i++) {
				if (i == idx-1) {
					sprintf(temp, "%d\n", data[i]);
				} else {
					sprintf(temp, "%d + ", data[i]);
				}
				strcat(buf, temp);
			}
			printf("%s", buf);
		} else {
			printf("%d is NOT perfect.\n", n);
		}
		scanf("%d", &n);
	}

	return 0;
}