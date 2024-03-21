n = int(input())
costs = []

for _ in range(n):
    costs.append(list(map(int, input().split())))

visited = [False] * (n+1)
selected = []
res = int(1e9)


def calc():
    temp_res = costs[0][selected[0] - 1]

    for i in range(len(selected) - 1):
        temp_res += costs[selected[i] - 1][selected[i + 1] - 1]

    temp_res += costs[selected[len(selected) - 1] - 1][0]

    return temp_res


def dfs(cur_num):
    global res
    if cur_num == n-1:
        # 계산
        res = min(res, calc())
        return 

    for i in range(2, n + 1):
        if visited[i]:
            continue
        
        visited[i] = True
        selected.append(i)

        dfs(cur_num + 1)

        selected.pop()
        visited[i] = False


dfs(0)
print(res)