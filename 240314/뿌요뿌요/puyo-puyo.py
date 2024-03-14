n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

cnt = 0
def dfs(x, y):
    val = arr[x][y]
    global cnt 
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and arr[nx][ny] == val and not visited[nx][ny]:
            visited[nx][ny] = True
            cnt += 1
            dfs(nx, ny)

total = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            cnt = 1
            dfs(i, j)

            total.append(cnt)

# print(total)
count = 0
for t in total:
    if t >= 4:
        count += 1

print(count, max(total))