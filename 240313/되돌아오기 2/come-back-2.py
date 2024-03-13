n = input()

# N 부터 오른쪽으로 90도 회전 기준으로 작성
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

x, y = 0, 0
d = 0
cnt = 0

for i in range(len(n)):
    cnt += 1
    if n[i] == 'F':
        x, y = x + dxs[d], y + dys[d]
        # print(x, y)
        if x == 0 and y == 0:
            break

    if n[i] == 'L':
        d = (d - 1) if d > 0 else 3
    if n[i] == 'R':
        d = (d + 1) % 4

print(cnt)