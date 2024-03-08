import sys

n = int(input())
points = []


MAX_POINT = -int(1e9)
for _ in range(n):
    point, alpha = map(str, input().split())
    points.append((int(point), alpha))
    MAX_POINT = max(MAX_POINT, int(point))

res = -1

points = sorted(points, key = lambda x: x[0])
# print(points)

def calc(i):
    g_cnt = 0
    h_cnt = 0
    val = 0

    for j in range(i, len(points)):
        if points[j][1] == 'G':
            g_cnt += 1
        elif points[j][1] == 'H':
            h_cnt += 1
        
        if g_cnt == h_cnt or g_cnt == j - i + 1 or h_cnt == j - i + 1:
            val = max(val, points[j][0] - points[i][0])

    return val



for i in range(len(points)):
    res = max(res, calc(i))

print(res)