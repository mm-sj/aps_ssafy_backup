N, M = map(int,input().split())
Nrr = [list(map(int,input().split())) for _ in range(N)]
Mrr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    lst = []
    for j in range(M):
        lst.append(Nrr[i][j]+Mrr[i][j])
    print(*lst)