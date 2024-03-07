import sys
from collections import defaultdict

n = input()
n_list = list(n)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f']

my_alpha = []

for item in n_list:
    if item in alphabet and item not in my_alpha:
        my_alpha.append(item)

val_dict = defaultdict(int)
res = -int(1e9)

def calc():
    val = val_dict[n_list[0]]
    stack = []

    for idx in range(1, len(n_list)):
        if n_list[idx] in alphabet:
            mode = stack.pop() if stack else '+'
            if mode == "+":
                val += val_dict[n_list[idx]]
            elif mode == "-":
                val -= val_dict[n_list[idx]]
            elif mode == "*":
                val *= val_dict[n_list[idx]]
        else:
            stack.append(n_list[idx])
    
    return val

def dfs(cnt):
    global res
    if cnt == len(my_alpha):
        res = max(res, calc())
        return 
    
    for i in range(1, 5):
        val_dict[my_alpha[cnt]] = i
        dfs(cnt + 1)

dfs(0)
print(res)