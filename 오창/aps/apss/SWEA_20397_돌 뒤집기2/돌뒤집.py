import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1,1+T):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(M):
        i, j = map(int,input().split())

        for k in range(1, j + 1):
            L = i - k - 1
            R = i + k - 1
            if L < 0 or R >= N:
                break
            if arr[L] == arr[R]:
                arr[L] = 1 - arr[L]
                arr[R] = arr[L]

    print(arr)






