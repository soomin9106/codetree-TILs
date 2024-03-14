n, t = map(int, input().split())

command = input()

arrs = []
for _ in range(3):
    arrs.append(list(map(int, input().split())))

# 오른쪽 돌기 기준
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


x, y = (n- 1)//2, (n- 1)//2
d = 0
res = arrs[x][y]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for i in range(t):
    if command[i] == 'F':
        nx, ny = x + dxs[d], y + dys[d]
        # print(nx, ny)
        if in_range(nx, ny):
            x, y = nx, ny
            res += arrs[x][y]

    elif command[i] == 'R':
        d = (d + 1) % 4

    else:
        d = (d - 1) if d != 0 else 3

print(res)