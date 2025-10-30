import sys
sys.stdin = open('input.txt')

arr = [list(map(int,input().split())) for _ in range(9)]

maxnum = 0
r, c = 0, 0
for i in range(9):
    for j in range(9):
        maxnum = max(maxnum, arr[i][j])
        if arr[i][j] == maxnum:
            r,c = i+1, j+1

print(maxnum)
print(r, c)






