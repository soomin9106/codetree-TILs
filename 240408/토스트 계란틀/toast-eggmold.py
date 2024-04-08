from collections import deque

n, l, r = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(x, y, visited):
    points = []
    q = deque()

    q.append((x, y))
    visited[x][y] = True
    points.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny) and not visited[nx][ny] and l <= abs(arr[nx][ny] - arr[cur_x][cur_y]) <= r:
                q.append((nx, ny))
                points.append((nx, ny))
                visited[nx][ny] = True

    sum_val = 0

    for p in points:
        sum_val += arr[p[0]][p[1]]

    avg = sum_val // len(points)

    for p in points:
        arr[p[0]][p[1]] = avg

    return len(points)


def simulate():
    visited = [[False] * n for _ in range(n)]
    isChanged = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                count = bfs(i, j, visited)
                if count > 1:
                    isChanged = True

    if not isChanged:
        # 계란 이동이 없는 경우
        return False

    return True

answer = 0
for _ in range(2):
    isChanged = simulate()

    # for i in range(n):
    #     for j in range(n):
    #         print(arr[i][j], end = ' ')
    #     print()
    # print(isChanged)
    if not isChanged:
        break
    else:
        answer += 1

print(answer)