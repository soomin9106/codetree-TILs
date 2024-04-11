n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)

def dfs(vertex):
    for cur_v in graph[vertex]:
        if not visited[cur_v]:
            visited[cur_v] = True
            dfs(cur_v)

dfs(1)

cnt = 0

for i in range(1, n + 1):
    if visited[i]:
        cnt += 1

cnt -= 1

if cnt == -1:
    print(0)
    exit(0)

print(cnt)