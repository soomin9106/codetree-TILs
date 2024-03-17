from collections import deque

n, m = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

visited = [[False]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def calc_cost(i, j, k):
    visited[i][j] = True

    q = deque()
    q.append((i, j, 0)) # depth 를 따로 관리 해줘야 해당 요소가 몇번째 돌고 있는지 확인할 수 있음
    map_cnt = (k * k) + (k+1)*(k+1)
    gold_cnt = maps[i][j]

    while q:
        cur_x, cur_y, cur_depth = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny) and not visited[nx][ny] and cur_depth < k:
                visited[nx][ny] = True
                q.append((nx, ny, cur_depth + 1))
                gold_cnt += maps[nx][ny]
            
    # print(gold_cnt, map_cnt)
    return gold_cnt


count_res = 0

for i in range(n):
    for j in range(n):
        for k in range(n+1):
            visited = [[False]*n for _ in range(n)]
            count = calc_cost(i, j, k)
            result_dug = (k * k) + (k+1)*(k+1)
            cost = (m * count) - result_dug
            if cost >= 0:
                count_res = max(count_res, count)

print(count_res)