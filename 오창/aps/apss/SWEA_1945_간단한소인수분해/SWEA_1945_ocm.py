import sys
sys.stdin = open('input.txt')

operator = [2, 3, 5, 7, 11]

T = int(input())
for tc in range(1,1+T):
    N = int(input())
    lst = []

    for i in range(len(operator)):
        while N % operator[i] == 0:
            lst.append(operator[i])
            N = N // operator[i]
    a = lst.count(2)
    b = lst.count(3)
    c = lst.count(5)
    d = lst.count(7)
    e = lst.count(11)
    print(f'#{tc}',a,b,c,d,e)