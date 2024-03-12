from sortedcontainers import SortedSet

c, n = map(int, input().split())

reds = []
blacks = []

for _ in range(c):
    reds.append(int(input()))

for _ in range(n):
    a, b = map(int, input().split())
    blacks.append((a, b))


blacks = sorted(blacks, key = lambda x: x[1])
red_s = SortedSet(reds)

ans = 0

for a, b in blacks:
    idx = red_s.bisect_left(a)
    if idx != len(red_s):
        ti = red_s[idx]

        if ti <= b:
            ans += 1
            red_s.remove(ti)

print(ans)