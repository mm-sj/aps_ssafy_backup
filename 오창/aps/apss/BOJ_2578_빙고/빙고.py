'''
빙고가 세줄이 되는 숫자의 인덱스
'''

player = [list(map(int, input().split())) for _ in range(5)]
host = []
for _ in range(5):
    host += list(map(int,input().split()))
pos_host = [0]*26
for i in range(5):
    for j in range(5):
        pos_host[player[i][j]] = (i, j)

v = [[0]*10 for _ in range(4)]   # v0~v3 빈도수 체크
# 사회자가 부르는 좌표를 읽어서, 빈도수체크, 5인 개수가 3개 이상이면 종료
for n in host:
    i, j = pos_host[n]       # 번호에서 좌표를 읽어옴
    v[0][j]+=1              # 세로 개수를 누적
    v[1][i]+=1              # 가로 개수를 누적
    v[2][i-j]+=1            # 우측아래 대각선 개수를 누적
    v[3][i+j]+=1            # 우측위쪽 대각선 개수를 누적
    cnt = 0
    for tlst in v:
        cnt += tlst.count(5)# 5개인 개수(한 줄 완성된 개수)
    if cnt>=3:              # 3개 이상이면 빙고!
        break
print(sum(v[0]))            # 표시(누적)된 개수가 불러준 숫자의 개수