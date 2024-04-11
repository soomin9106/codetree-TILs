n = int(input())

visited = [[0] * n for _ in range(n)]

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, val):
    return in_range(x, y) and \
            not visited[x][y] and \
            arr[x][y] == val

def dfs(x, y, num):
    visited[x][y] = num

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny, arr[x][y]):
            visited[nx][ny] = num
            dfs(nx, ny, num)

cnt = 1

def calc():
    max_cnt = 0
    bomb_cnt = 0
    for i in range(1, cnt):
        temp_cnt = 0

        for k in range(n):
            for l in range(n):
                if visited[k][l] == i:
                    temp_cnt += 1

        if temp_cnt >= 4:
            bomb_cnt += 1

        if max_cnt < temp_cnt:
            max_cnt = temp_cnt

    return bomb_cnt, max_cnt

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, cnt)
            cnt += 1

# print(visited, cnt)

bomb_cnt, max_cnt = calc()

print(bomb_cnt, max_cnt)