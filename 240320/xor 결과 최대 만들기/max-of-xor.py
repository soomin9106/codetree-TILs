n, m = map(int, input().split())
arr = list(map(int, input().split()))

selected_nums = []
res = -int(1e9)

def calc_xor():
    # selected_nums 에 있는 값들 xor 계산
    # print(selected_nums)
    val = selected_nums[0]

    for i in range(1, len(selected_nums)):
        val ^= selected_nums[i]
    
    return val

def dfs(idx):
    global selected_nums 
    global res
    if len(selected_nums) == m:
        res = max(calc_xor(), res)
        return 
    
    if idx >= n:
        return

    selected_nums.append(arr[idx])
    dfs(idx + 1)
    selected_nums.pop()

    dfs(idx + 1)

dfs(0)
print(res)