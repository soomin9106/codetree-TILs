n = int(input())

cnt = 100000

for i in range(0, 100001):
    r = n - (5 * i)
    if r >= 0 and r % 2 == 0:
        cnt = min(cnt, i + (r // 2))

if cnt == 100000:
    print(-1)
    exit(0)

print(cnt)