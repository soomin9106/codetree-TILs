from collections import defaultdict

n, k = map(int, input().split())

start = 0

segments = []

for _ in range(n):
    dist, d = map(str, input().split())
    dist = int(dist)

    if d == 'L':
        segments.append((start - dist, start))
        start -= dist

    else:
        segments.append((start, start + dist))
        start += dist

points = []

for x1, x2 in segments:
    points.append((x1, +1))
    points.append((x2, -1))

points.sort()

ans = 0
sum_val = 0

for idx, (x, v) in enumerate(points):
    if sum_val >= k:
        prev_x, _ = points[idx - 1]
        ans += (x - prev_x)

    sum_val += v


print(ans)