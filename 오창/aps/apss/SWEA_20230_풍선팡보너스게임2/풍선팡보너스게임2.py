import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    ans2 = float('inf')
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            m = arr[i][j]
            for r, c in [[1,0],[0,1],[-1,0],[0,-1]]:
                for k in range(1,N):
                    nr, nc = i + r * k, j + c * k
                    if 0 <= nr < N and 0 <= nc < N:
                        s += arr[nr][nc]
                        m += arr[nr][nc]
            ans = max(ans, s)
            ans2 = min(ans2, m)

    print(f'#{tc}',ans-ans2)