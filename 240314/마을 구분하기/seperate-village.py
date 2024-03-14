n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

def dfs(x, y):
    global cnt
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] == 1:
            visited[nx][ny] = True

            cnt += 1
            dfs(nx, ny)


cnt = 0
people = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            cnt = 1

            dfs(i, j)

            people.append(cnt)


people.sort()
print(len(people))

for p in people:
    print(p)