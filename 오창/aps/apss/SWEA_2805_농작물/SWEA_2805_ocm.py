import sys
sys.stdin = open('input.txt')
'''
가로세로길이 N인 마름모 면적내의 합 구하기 

위,아래 따로 피라미드식으로
arr[N//2] (중간)기준으로 위아래

'''
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int,input().strip())) for _ in range(N)]
    center = N // 2
    total = 0

    for i in range(N):
        if i <= center:
            total += sum(arr[i][center - i : center + i + 1])
        else:
            diff = i - center
            total += sum(arr[i][diff : N - diff])

    print(f'#{tc}',total)