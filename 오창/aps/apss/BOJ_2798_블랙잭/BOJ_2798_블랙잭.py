import sys
sys.stdin = open('input.txt')

from itertools import combinations

N, M = map(int,input().split())
arr = list(map(int,input().split()))
combi = list(combinations(arr,3))
lst = []
for i in range(len(combi)):
    lst.append(sum(combi[i]))
lst.sort()
s = 0
for i in range(len(lst)):
    if lst[i] <= M:
        s = lst[i]
print(s)