import sys
sys.stdin = open('sample_in.txt')
'''
상하좌우에서 더 낮은 영역으로만 이동
그 중에서 최솟값
최대 길이
'''

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            while True:
                mini, minj = i, j
                for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < N and 0 <= nc < N and arr[mini][minj] > arr[nr][nc]:
                        mini, minj = nr, nc
                if arr[i][j] > arr[mini][minj]:
                    i, j = mini, minj
                    cnt += 1
                else:
                    if result < cnt:
                        result = cnt
                    break
    print(result)

    '''
    1부터 N 까지
               20         31
         20         24            31
      20   22    24    26     28    31
    20 21 22 23 24 25 26 27 28 29 30 31
    1 2 3 4 5 
    1 2 1라
    1 3 2라
    1 4 2라
    1 5 3라라
   '''