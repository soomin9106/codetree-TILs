import sys

n = int(input())
bomb_type = [[0] * n for _ in range(n)]
bombed = [[False] * n for _ in range(n)]
res = 0

bomb_pos = []

bomb_shapes = [
    [],
    [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
    [(-1, 0), (0, -1), (0, 0), (1, 0), (0, 1)],
    [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]
]

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def bomb(x, y, b_type):
    for i in range(5):
        nx, ny = x + bomb_shapes[b_type][i][0], y + bomb_shapes[b_type][i][1]
        if inRange(nx, ny):
            bombed[nx][ny] = True


def calc():
    for i in range(n):
        for j in range(n):
            bombed[i][j] = False
    
    for i in range(n):
        for j in range(n):
            if bomb_type[i][j]:
                bomb(i, j, bomb_type[i][j])
    
    cnt = 0

    for i in range(n):
        for j in range(n):
            if bombed[i][j]:
                cnt += 1
    
    return cnt



def dfs(cnt):
    global res

    if cnt == len(bomb_pos):
        res = max(res, calc())
        return 

    for i in range(1, 4):
        x, y = bomb_pos[cnt]

        bomb_type[x][y] = i
        dfs(cnt + 1)
        bomb_type[x][y] = 0

for i in range(n):
    row = list(map(int, input().split()))
    for j, bomb_place in enumerate(row):
        if bomb_place:
            bomb_pos.append((i, j))


dfs(0)

print(res)