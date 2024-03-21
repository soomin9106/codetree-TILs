n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

visited_row = [False] * n
visited_col = [False] * n
selected_elements = []
res = -int(1e9)

def dfs(cur_num, x, y):
    global res
    if cur_num == n:
        res = max(res, sum(selected_elements))
        return

    for i in range(n):
        if visited_row[i]:
            continue
        
        visited_row[i] = True
        for j in range(n):
            if visited_col[j]:
                continue
            visited_col[j] = True
            selected_elements.append(arr[i][j])
            dfs(cur_num + 1, i, j)
            selected_elements.pop()
            visited_col[j] = False
        
        visited_row[i] = False

dfs(0, 0, 0)
print(res)