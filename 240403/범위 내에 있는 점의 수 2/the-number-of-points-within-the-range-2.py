n, q = map(int, input().split())

points = list(map(int, input().split()))



points.sort()
max_point = max(points)

prefix_sum = [0] * (max_point + 1)
for i in range(1, max_point + 1):
    flag = 0
    if i in points:
        flag = 1
    
    prefix_sum[i] = prefix_sum[i - 1] + flag

answer = 0
for _ in range(q):
    s, e= map(int, input().split())
    flags = 0
    if s in points:
        flags = 1
    if s > max_point:
        print(0)
    elif e > max_point and s < max_point:
        print(max(prefix_sum) - prefix_sum[s] + flags)
    else:
        print(prefix_sum[e] - prefix_sum[s] + flags)