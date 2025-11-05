import sys
sys.stdin = open('sample_in.txt')


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                    for m in range(N):
                        nr, nc = i + dr * m, j + dc * m
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 0:
                                arr[nr][nc] = 3
                            if arr[nr][nc] == 1:
                                break
    cnt = 0
    for i in arr:
        cnt += i.count(0)
    print(f'#{tc}',cnt)