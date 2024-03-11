n = int(input())

cnt = 0

arr = [5, 2]

for a in arr:
    cnt += (n // a)
    n %= a

if n != 0:
    print(-1)
    exit(0)

print(cnt)