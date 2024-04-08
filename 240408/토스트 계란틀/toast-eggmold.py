from collections import deque

n, l, r = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(x, y):
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

    sum_val = sum([
        arr[x][y]
        for x, y in points
    ])

    for p in points:
        arr[p[0]][p[1]] = sum_val // len(points)

    return len(points)

# visited 배열을 초기화 해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def simulate():
    initialize_visited()

    isChanged = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                count = bfs(i, j)
                if count > 1:
                    isChanged = True

    if not isChanged:
        # 계란 이동이 없는 경우
        return False

    return True

answer = 0
for _ in range(2000):
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