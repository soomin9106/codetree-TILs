import sys

n = int(input())
lines = []

for _ in range(n):
    lines.append(list(map(int, input().split())))

lines = sorted(lines, key = lambda x: x[0])


res = -int(1e9)
def dfs(level, arr):
    global res
    if level == len(lines):
        res = max(res, len(arr))
        return
    
    for i in range(len(lines)):
        if not arr or arr[-1] != lines[i] and arr[-1][1] < lines[i][0]:
            arr.append(lines[i])
            dfs(level + 1, arr)
            # arr.pop()

dfs(1, [])
print(res)