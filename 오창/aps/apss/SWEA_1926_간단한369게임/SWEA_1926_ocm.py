'''
count 에따라 --- 개수 999면 ---

'''
N = int(input())
arr = [str(i) for i in range(N+1)][1:N+1]

for i in arr:
    lst = i.replace('3', '-').replace('6', '-').replace('9', '-')
    if '-' in lst:
        print('-' * lst.count('-'), end=' ')
    else:
        print(i, end=' ')