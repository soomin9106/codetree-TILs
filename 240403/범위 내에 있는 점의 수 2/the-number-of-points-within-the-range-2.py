n, q = map(int, input().split())

points = list(map(int, input().split()))

max_point = max(points)

nums = [0] * (max_point + 1)
for point in points:
    nums[point] = 1

prefix_sum = [0] * (max_point + 1)
for i in range(1, max_point + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i]

answer = 0
for _ in range(q):
    s, e= map(int, input().split())

    if s > max_point:
        print(0)
    elif e > max_point and s < max_point:
        print(max(prefix_sum) - prefix_sum[s] + nums[s])
    else:
        print(prefix_sum[e] - prefix_sum[s] + nums[s])