import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    cnt = set()
    k = 0
    while len(cnt) < 10:
        k += 1
        sheep = k * N
        cnt.update(str(sheep))
    print(f'#{tc}',sheep)