import sys
sys.stdin = open('in1.txt')


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # +
    cross = 0
    xcross = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                for m in range(1, M):
                    nr, nc = dr * m + i, dc * m + j
                    if 0 <= nr < N and 0 <= nc < N:
                        s += arr[nr][nc]
            cross = max(cross, s)
            u = arr[i][j]
            for di, dj in [[1, 1], [-1, 1], [1, -1], [-1, -1]]:
                for k in range(1, M):
                    ni, nj = di * k + i, dj * k + j
                    if 0 <= ni < N and 0 <= nj < N:
                        u += arr[ni][nj]
            xcross = max(xcross, u)
    print(f'#{tc}', max(cross, xcross))