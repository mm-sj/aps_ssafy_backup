import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, 1+T):
    N,M = map(int,input().split())
    Nrr = list(map(int,input().split()))
    Mrr = list(map(int,input().split()))
    max_hap = -float('inf')

    if N > M:
        N, M = M, N
        Nrr, Mrr = Mrr, Nrr

    for i in range(M-N):
        hap = 0
        for j in range(N):
            hap += Nrr[j] * Mrr[i+j]
        max_hap = max(max_hap, hap)

    print(max_hap)