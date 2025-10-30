import sys
sys.stdin = open('input1.txt')


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxlng = 0
    # 가로 cnt 하다가 0 만나면 초기화 max
    lst = []
    for i in range(N):
        for j in range(N):
            print(arr[i][j], arr[j][i])
