import sys

n = int(input())

res = []

def dfs(level, val):
    global res
    if level == n:
        res.append(val)
        return 
    
    for i in range(1, 5):
        temp = str(i) * i
        if len(temp) > n:
            return 
        elif level + len(temp) > n:
            return 
        else:
            dfs(level + len(temp), val + temp)

dfs(0, "")

print(len(res))