n = int(input())
costs = []

for _ in range(n):
    costs.append(list(map(int, input().split())))

visited = [False] * (n)
selected = []
res = int(1e9)



def dfs(cur_num):
    global res
    if cur_num == n:
        # 계산
        total_cost = 0
        for j in range(n - 1):
            cur_cost = costs[selected[j]][selected[j+1]]
            if cur_cost == 0:
                return 
            total_cost += cur_cost
        additional_cost = costs[selected[-1]][0]
        if additional_cost == 0:
            return 
        
        res = min(res, total_cost + additional_cost)
        return 

    for i in range(1, n):  
        if visited[i]:
            continue
        
        visited[i] = True
        selected.append(i)

        dfs(cur_num + 1)

        selected.pop()
        visited[i] = False

visited[0] = True
selected.append(0)
dfs(1)

print(res)