from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]
q = deque()

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


hospitals = []
selected_hospitals = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            hospitals.append((i, j))

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and arr[x][y] != 1

def calc():
    cnt = 0
    while q:
        cur_x, cur_y, cur_sec = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny, cur_sec + 1))
                cnt = max(cur_sec + 1, cnt)

    # 모든 바이러스를 치유하지 못한 경우
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] == 0:
                return -1

    return cnt
    
ans = int(1e9)
def choose_hospitals(idx):
    global ans
    if len(selected_hospitals) == m:
        initialize_visited()
        for x, y in selected_hospitals:
            q.append((x, y, 0))
        val = calc()

        # 모든 바이러스를 제거할 수 없는 경우
        if val == -1:
            return 

        ans = min(ans, val)
        return

    if idx >= len(hospitals):
        return

    choose_hospitals(idx + 1)

    selected_hospitals.append(hospitals[idx])
    choose_hospitals(idx + 1)
    selected_hospitals.pop()

choose_hospitals(0)
if ans == int(1e9):
    print(-1)
    exit(0)

print(ans)