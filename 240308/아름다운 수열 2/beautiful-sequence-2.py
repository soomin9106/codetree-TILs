import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_len = len(a)
b_len = len(b)

cnt = 0

for i in range(a_len - b_len + 1):
    one_lst = a[i: i+m]
    flag = True
    for item in one_lst:
        if item in b:
            continue
        else:
            flag = False
            break
    
    if flag:
        cnt += 1


print(cnt)