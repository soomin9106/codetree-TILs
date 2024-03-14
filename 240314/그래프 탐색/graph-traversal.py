from collections import defaultdict

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(x):
    visited[x] = True
    for item in graph[x]:
        if not visited[item]:
            visited[item] = True
            dfs(item)


dfs(1)
print(visited.count(True) - 1)