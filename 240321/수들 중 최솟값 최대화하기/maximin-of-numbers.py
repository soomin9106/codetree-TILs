n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

selected = []
ans = -int(1e9)
visited_col = [False] * n

def get_minimum_in_selected():
    res = int(1e9)
    for i in range(len(selected)):
        res = min(res, arr[i][selected[i]])
    
    return res

def dfs(cur_num):
    global ans
    if cur_num == n:
        ans = max(ans, get_minimum_in_selected())
        return 

    for i in range(n):
        if visited_col[i]:
            continue

        visited_col[i] = True
        selected.append(i)
        dfs(cur_num + 1)
        selected.pop()
        visited_col[i] = False

dfs(0)
print(ans)