import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxarr = 0
    r, c = 0, 0
    for i in range(N):
        for j in range(N):
            maxarr = max(maxarr, arr[i][j])
            r, c = i, j

    cnt = 1
    while True:
        s = arr[r][c]
        minval = s
        minr, minc = r, c
        for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
            nr, nc = r + dr, c+ dc
            if 0 <= nr < N and 0 <= nc < N:
                minval = min(minval, arr[nr][nc])
                minr,minc = nr, nc
        if minval >= s:
            break
        r, c = minr, minc
        cnt += 1

    print(cnt)
    