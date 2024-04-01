from collections import deque

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

# 2의 위치 기억
twos = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            twos.append((i, j))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def init_temp():
    temp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[i][j]

    return temp

def bfs():
    temp = init_temp()
    q = deque()
    visited = [[False] * m for _ in range(n)]
    for t in twos:
        x, y = t
        q.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny) and temp[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                temp[nx][ny] = 2
                q.append((nx, ny))

    ans = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                ans += 1

    return ans

answer = -int(1e9)
def backtracking(cur_num):
    global answer
    if cur_num == 3:
        val = bfs()
        answer = max(answer, val)
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                backtracking(cur_num + 1)
                arr[i][j] = 0

backtracking(0)
print(answer)