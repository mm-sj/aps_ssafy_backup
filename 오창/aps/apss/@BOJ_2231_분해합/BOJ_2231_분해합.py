import sys
sys.stdin = open('input.txt')

N = int(input())
result = 0  # 생성자 저장용

for i in range(1, N):
    # 각 자리수 합 구하기
    digits_sum = sum(map(int, str(i)))
    if i + digits_sum == N:
        result = i
        break

print(result)
