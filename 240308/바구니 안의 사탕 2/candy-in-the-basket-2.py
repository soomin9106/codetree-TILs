import sys 

n, k = map(int, input().split())
buckets = [0 for i in range(101)]
max_point = -int(1e9)
for _ in range(n):
    cnt, point = map(int, input().split())
    buckets[point] += cnt
    max_point = max(max_point, point)

# print(buckets)

res = -int(1e9)

for i in range(max_point + 1):
    val = 0
    for j in range(i - k, i + k + 1):
        if 0 <= j <= 100:
            val += buckets[j]

    res = max(res, val)

print(res)