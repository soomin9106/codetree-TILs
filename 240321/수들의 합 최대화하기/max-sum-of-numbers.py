n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

visited_row = [False] * n
visited_col = [False] * n
selected_elements = []
res = -int(1e9)

def calc():
    temp_res = 0
    for i in range(n):
        temp_res += arr[i][selected_elements[i]]

    return temp_res

def dfs(cur_num):
    global res
    if cur_num == n:
        res = max(res, calc())
        return

    for j in range(n):
        if visited_col[j]:
            continue
        visited_col[j] = True
        selected_elements.append(j)
        dfs(cur_num + 1)
        selected_elements.pop()
        visited_col[j] = False

dfs(0)
print(res)