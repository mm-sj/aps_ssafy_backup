import sys
sys.stdin = open('sample_input(1).txt')

T = int(input())
for tc in range(1,1+T):
    N, M = map(int,input().split())
    arr = [[0]*(N) for _ in range(N)]
    arr[N // 2][N // 2], arr[N // 2 - 1][N // 2 - 1] = 2, 2
    arr[N // 2][N // 2 - 1], arr[N // 2 - 1][N // 2] = 1, 1

    for _ in range(M):
        x, y, color = map(int, input().split())
        arr[x-1][y-1] = color

        for r,c in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
            lst = []
            for k in range(1, N):
                nr, nc = x-1 + r * k, y-1  + c * k
                if not (0 <= nr < N and 0 <= nc < N):
                    break

                if arr[nr][nc] == 0:
                    break

                if arr[nr][nc] == color:
                    for rr, cc in lst:
                        arr[rr][cc] = color
                    break
                else:
                    lst.append((nr,nc))

    for i in arr:
        print(i)
