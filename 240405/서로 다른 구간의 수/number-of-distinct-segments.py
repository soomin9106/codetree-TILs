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

segs = set()

ans = 0
for x, v, index in points:
    if v == +1: # 시작점인 경우 
        if not segs: # 아무 선분도 없을 때는 ans 갱신
            ans += 1

        segs.add(index) # 합쳐야 될 선분 목록에 넣어줌

    else: # 끝점인 경우는 그 선분을 지워줌
        segs.remove(index)

print(ans)