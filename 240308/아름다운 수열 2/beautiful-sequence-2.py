import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_len = len(a)
b_len = len(b)

cnt = 0

for i in range(a_len - b_len + 1):
    if sorted(a[i: i+m]) == sorted(b):
        cnt += 1


print(cnt)