n = int(input())

segments = []

for _ in range(n):
    s, e = map(int, input().split())
    segments.append((s, e))

points = []
for idx, (x1, x2) in enumerate(segments):
    points.append((x1, +1, idx))
    points.append((x2, -1, idx))

points.sort()

start = 0 
end = 0
answer = 0
ans = 0
segs = set()

for x, v, index in points:
    if v == 1:
        if not segs:
            ans += (end - start)
            start = x
            answer += 1

        segs.add(index)
    else:
        end = x
        segs.remove(index)

ans += (end - start)

print(ans)