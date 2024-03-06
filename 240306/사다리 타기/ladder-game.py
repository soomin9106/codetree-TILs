import sys

n, m = map(int, input().split())

lines = []
selected_lines = []
res = m

for _ in range(m):
    a,b = map(int, input().split())
    lines.append((b, a))

lines.sort()

def get_initial_list():
    nums = [i for i in range(0, n+1)]

    for _, line in lines:
        nums[line], nums[line + 1] = nums[line + 1], nums[line]
    
    return nums[1:]

def calc():
    nums_original = get_initial_list()

    nums = [i for i in range(0, n+1)]

    for _, line in selected_lines:
        nums[line], nums[line + 1] = nums[line + 1], nums[line]
    
    if nums_original == nums[1:]:
        return True
    
    return False


def dfs(cnt):
    global res
    if cnt == m:
        if calc():
            res = min(res, len(selected_lines))
        return 
    
    selected_lines.append(lines[cnt])
    dfs(cnt + 1)
    selected_lines.pop()

    dfs(cnt + 1)


dfs(0)
print(res)