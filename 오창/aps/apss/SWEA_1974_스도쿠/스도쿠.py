import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,1+T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    arr2 = list(zip(*arr))
    N = 9
    ans = 1

    for i in range(N):
        s = 0
        for j in range(N):
            s += arr[i][j]
        if s != 45:
            ans = 0
            break

    if ans:
        for i in range(N):
            d = 0
            for j in range(N):
                d += arr2[i][j]
            if d != 45:
                ans = 0
                break
    if ans:
        for i in range(0,N,3):
            for j in range(0,N,3):
                h = 0
                for r in range(3):
                    for c in range(3):
                        nr, nc = i+r, j+c
                        if 0 <= nr < N and 0 <= nc < N:
                            h += arr[nr][nc]
                if h != 45:
                    ans = 0
                    break
    print(f'#{tc}',ans)