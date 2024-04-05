n = int(input())

points = []

for _ in range(n):
    s, e = map(int, input().split())
    points.append((s, +1))
    points.append((e, -1))

points.sort()

res = 0
cur = 0
for x, v in points:
    overlapped_val = cur + v
    cur = cur + v
    res = max(res, overlapped_val)

print(res)