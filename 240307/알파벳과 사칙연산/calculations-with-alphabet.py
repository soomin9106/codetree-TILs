import sys

n = input()
n_list = list(n)

res = -int(1e9)
modes = ['+', '-', '*']
my_modes = []
my_alphas = []

for item in n_list:
    if item in modes:
        my_modes.append(item)
    else:
        my_alphas.append(item)

changed_nums = [0] * len(my_alphas)


def calc():
    val = changed_nums[0]
    idx = 1
    
    for mode in my_modes:
        if mode == '+':
            val += changed_nums[idx]
        elif mode == '-':
            val -= changed_nums[idx]
        elif mode == '*':
            val *= changed_nums[idx]
        idx += 1
    
    return val

def dfs(cnt):
    global res
    if cnt == len(my_alphas):
        val = calc()
        res = max(res, val)
        return
    
    for i in range(1, 5):
        
        changed_nums[cnt] = i
        dfs(cnt + 1)
        

dfs(0)
print(res)