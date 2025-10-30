import sys
sys.stdin = open('input.txt')
T = 2
'''
c = cloud
. = c 가 우측으로 가야 할 경로
cnt = -1 로 가면서 c를 만나면 c+=1
'''
for tc in range(1,1+T):
    H, W = map(int, input().split())
    arr = [list(map(str,input().strip())) for _ in range(H)]


    for i in range(H):
        cnt = -1 #-1 로 채움
        for j in range(W):
            if arr[i][j] == 'c': #c를 만나면
                cnt = 0 #cnt 0 으로 만들고 채우기
                arr[i][j] = cnt

            else: #c 가 아니고
                if cnt >= 0: #c가 0보다 크면
                    cnt += 1 #cnt 1 더하고 채우기
                arr[i][j] = cnt

    for i in range(H):
        print(*arr[i])