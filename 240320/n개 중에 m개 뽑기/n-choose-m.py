n, m = map(int, input().split())

nums = [i for i in range(1, n + 1)]
selected_nums = []

def print_nums():
    for num in selected_nums:
        print(num, end = ' ')
    print()

# def dfs(idx):
#     global selected_nums
#     if len(selected_nums) == m:
#         print_nums()
#         return

#     if idx >= n:
#         return

#     selected_nums.append(nums[idx])
#     dfs(idx + 1)
#     selected_nums.pop()
#     dfs(idx + 1)

def dfs(cnt, last_num):
    global selected_nums
    if cnt == m:
        print_nums()
        return 

    for i in range(last_num + 1, n + 1):
        selected_nums.append(i)
        dfs(cnt + 1, i)
        selected_nums.pop()


for num in nums:
    selected_nums.append(num)
    dfs(1, num)
    selected_nums.pop()