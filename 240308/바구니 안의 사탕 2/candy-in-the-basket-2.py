import sys 

n, k = map(int, input().split())
buckets = [(i, 0) for i in range(101)]
max_point = -int(1e9)
for _ in range(n):
    cnt, point = map(int, input().split())
    max_point = max(max_point, point)
    buckets[point] = (point, cnt)

# print(buckets)

res = -int(1e9)

for i in range(max_point + 1):
    val = 0
    for j in range(i - k, i + k + 1):
        if j < 1 or j > 100:
            break
        val += buckets[j][1]

    res = max(res, val)

print(res)