from collections import deque

n, k, u, d = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

max_res = -int(1e9)
q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

# BFS 함수 수정
def bfs(combination):
    visited = [[False] * n for _ in range(n)]
    for x, y in combination:
        visited[x][y] = True
        q.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny) and not visited[nx][ny] and u <= abs(arr[nx][ny] - arr[cur_x][cur_y]) <= d:
                q.append((nx, ny))
                visited[nx][ny] = True

    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
    return cnt

# 백트래킹을 통해 k 개의 점을 고르기
def select_k(l, r, c, combination):
    global max_res
    if l == k:
        count = bfs(combination)
        max_res = max(max_res, count)
        return 

    for i in range(r, n):
        start_col = c if i == r else 0 
        for j in range(start_col, n):
            combination.append((i, j))
            select_k(l + 1, i, j, combination) 
            combination.pop()

select_k(0, 0, 0, [])

print(max_res)