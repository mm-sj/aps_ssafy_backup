import sys
sys.stdin = open('input.txt')

def recure(x,y):
    if y == Y:
        return x
    return x*recure(x, y+1)

T = 10
for tc in range(1,1+T):
    N = int(input())
    X,Y = map(int,input().split())
    re = recure(X,1)
    print(re)

    # print(pow(X,Y))