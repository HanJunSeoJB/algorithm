#include <stdio.h>
#include <stdlib.h>

int main() {
	int board[20][20] = { 0, };
	int N, i, j;
	int start, link = 0;
	int min = 500;
	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			scanf("%d ", &board[i][j]);
		}
	}
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			start = board[i][j] + board[j][i];
			link = board[i][j+1] + board[j + 1][i];
			if(j == N-1)
				link = board[i+1][j] + board[j][i+1];

			if (abs(start - link) < min) {
				min = abs(start - link);
			}
		}
	}
	printf("%d", min);
}