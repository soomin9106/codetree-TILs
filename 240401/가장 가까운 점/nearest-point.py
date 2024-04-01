import heapq

n, m = map(int, input().split())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

pq = []

def calc_dist(x, y):
    return abs(x) + abs(y)

for point in points:
    x, y = point
    heapq.heappush(pq, (calc_dist(x, y), x, y))

for _ in range(m):
    _, nx, ny = heapq.heappop(pq)

    heapq.heappush(pq, (calc_dist(nx + 2, ny + 2), nx + 2, ny + 2))

print(pq[0][1], pq[0][2])