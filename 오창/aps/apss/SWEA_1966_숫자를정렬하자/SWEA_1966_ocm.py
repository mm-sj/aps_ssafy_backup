import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,1+T):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    print(f'#{tc}',*arr)