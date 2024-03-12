from bisect import bisect_left

c, n = map(int, input().split())

reds = []
blacks = []

for _ in range(c):
    reds.append(int(input()))

for _ in range(n):
    a, b = map(int, input().split())
    blacks.append((a, b))

reds.sort()
blacks = sorted(blacks, key = lambda x: x[1])


ans = 0
visited = set()
for i in range(n):
    start, end = blacks[i]

    if start > reds[-1] or end < reds[0]:
        continue

    s_idx, e_idx = bisect_left(reds, start), bisect_left(reds, end)

    # print(s_idx, e_idx)
    if e_idx == len(reds):
        e_idx -= 1
    if s_idx == len(reds):
        s_idx -= 1

    while s_idx < len(reds) and reds[s_idx] in visited and s_idx <= e_idx:
        s_idx += 1
    
    if s_idx > e_idx or reds[s_idx] > end:
        continue
    else:
        ans += 1
        visited.add(reds[s_idx])

print(ans)