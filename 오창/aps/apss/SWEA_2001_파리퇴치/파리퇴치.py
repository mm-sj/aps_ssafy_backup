import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxkill = 0

    for i in range(N):
        for j in range(N):
            kill = 0
            for r in range(M):
                for c in range(M):
                    nr, nc = i + r, j + c
                    if 0 <= nr < N and 0 <= nc < N:
                        kill += arr[nr][nc]
            maxkill = max(kill,maxkill)
    print(f'#{tc}',maxkill)