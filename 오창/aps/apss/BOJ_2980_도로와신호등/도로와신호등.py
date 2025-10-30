'''
도로 끝까지 이동하는데 걸리는 시간

처음에 다같이 빨간불
      !    !
0 1 2 3 4 5 6 7 8 9 10


'''

N, L = map(int, input().split()) # N L
cnt = 0
for _ in range(N): # D위치 Red Green
    D, R, G = map(int,input().split())
