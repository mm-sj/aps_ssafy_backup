'''
설탕배달을 해야한다 정확하게 N 킬로그램
봉지는 3킬로와 5킬로인데 최소한의 봉지로
18이면 5킬로 3개와 3킬로 1개

'''
N = int(input())

for c5 in range(N//5, -1, -1):
    c3 = (N - c5 * 5)//3
    if c5 * 5 + c3 * 3 == N:
        print(c5 + c3)
        break
else:
    print(-1)
