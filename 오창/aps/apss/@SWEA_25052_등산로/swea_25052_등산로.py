import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            pi, pj = i, j
            m = arr[pi][pj]

            while True: # 더 이상 이동할 수 없을 때까지 반복

                ni, nj = pi, pj
                for r,c in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nr, nc = pi + r, pj + c
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] < m:
                            m = arr[nr][nc]
                            ni, nj = nr, nc
                if ni == pi and nj == pj:
                    break
                pi, pj = ni, nj
                cnt += 1
            result = max(result, cnt)

    print(result)