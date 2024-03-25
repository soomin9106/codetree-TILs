from collections import defaultdict

n = int(input())
points = defaultdict(list)

for _ in range(n):
    x, y = map(int, input().split())
    points[x].append((x, y))

for point in points:
    points[point] = sorted(points[point], key = lambda x: x[1])

ans = 0

for point in points:
    ans += points[point][0][1]

print(ans)