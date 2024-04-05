n = int(input())

points = []
max_point = 0
for _ in range(n):
    s, e = map(int, input().split())
    points.append((s, 1))
    points.append((e, -1))
    max_point = max(max_point, e)

points.sort()

res = 0
for i in range(max_point + 1):
    sum_val = 0
    for x, v in points:
        if x >= i:
            break

        sum_val += v
    
    res = max(res, sum_val)

print(res)