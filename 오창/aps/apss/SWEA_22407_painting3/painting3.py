import sys
sys.stdin = open('sample_in.txt')


T = int(input())
for tc in range(1, 1+T):
    arr = [[0] * 11 for _ in range(11)]
    x1, y1, x2, y2 = map(int, input().split())
    a1, b1, a2, b2 = map(int, input().split())

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[i][j] = 1
    for i in range(a1, a2+1):
        for j in range(b1, b2+1):
            if arr[i][j] == 1:
                arr[i][j] = 2
            else:
                arr[i][j] = 1

    w, h = 0, 0
    for i in range(len(arr)):
        ww = 0
        hh = 0
        for j in range(len(arr)):
            if arr[i][j] == 2:
                ww += 1
            if arr[j][i] == 2:
                hh += 1
        w = max(w, ww)
        h = max(h, hh)

    print(f'#{tc}',w,h)

