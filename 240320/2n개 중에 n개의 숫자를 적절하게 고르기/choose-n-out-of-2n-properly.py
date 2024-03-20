n = int(input())
arr = list(map(int, input().split()))
summ = sum(arr)

selected_nums = []
res = int(1e9)

def calc():
    sum1 = sum(selected_nums)
    sum2 = summ - sum1

    return abs(sum2 - sum1)

def dfs(cur_idx, cnt):
    global res, selected_nums
    if cnt == n:
        res = min(res, calc())
        return

    if cur_idx == 2 * n:
        return 

    dfs(cur_idx + 1, cnt)

    selected_nums.append(arr[cur_idx])
    dfs(cur_idx + 1, cnt + 1)
    selected_nums.pop()


dfs(0, 0)
print(res)