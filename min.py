n, m = map(int, input().split())

board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):

        white = 0
        black = 0

        # 구간의 첫 번째 칸의 색을 기준으로 흑백을 정함
        start_color = board[i][j]

        for a in range(i, i+8):
            for b in range(j, j+8):
                
                if (a + b) % 2 == 0:
                    if board[a][b] != start_color:
                        white += 1
                    else:
                        black += 1
                else:
                    if board[a][b] != start_color:
                        black += 1
                    else:
                        white += 1

        result.append(white)
        result.append(black)

print(result)
print(min(result))
