from collections import deque

n, l, r = map(int, input().split())

egg = []
for _ in range(n):
    egg.append(list(map(int, input().split())))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

visited = [[False] * n for _ in range(n)]
bfs_q = deque()
egg_group = []


def can_go(x, y, curr_egg):
    if not in_range(x, y):
        return False

    diff = abs(egg[x][y] - curr_egg)
    return not visited[x][y] and l <= diff <= r


def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def bfs():
    while bfs_q:
        cur_x, cur_y = bfs_q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if can_go(nx, ny, egg[cur_x][cur_y]):
                bfs_q.append((nx, ny))
                visited[nx][ny] = True
                egg_group.append((nx, ny))

def merge_eggs():
    sum_of_eggs = sum([
        egg[x][y]
        for x, y in egg_group
    ])

    for x, y in egg_group:
        egg[x][y] = sum_of_eggs // len(egg_group)

def move_eggs():
    global egg_group

    initialize_visited()

    is_changed = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                egg_group = []

                bfs_q.append((i, j))
                egg_group.append((i, j))
                visited[i][j] = True

                bfs()

                if len(egg_group) > 1:
                    is_changed = True

                merge_eggs()

    return is_changed

move_cnt = 0

while True:
    is_changed = move_eggs()
    if not is_changed:
        break

    move_cnt += 1

print(move_cnt)