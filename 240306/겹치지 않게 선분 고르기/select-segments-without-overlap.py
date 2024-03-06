import sys

n = int(input())
lines = []
selected_lines = []
res = 0

for _ in range(n):
    lines.append(list(map(int, input().split())))


def isOverlapped(l1, l2):
    x1, y1 = l1
    x2, y2 = l2

    return x1 <= x2 <= y1 or x1 <= y2 <= y1 or x2 <= x1 <= y2 or x2 <= y1 <= y2

def isPossible():
    for i, l1 in enumerate(selected_lines):
        for j, l2 in enumerate(selected_lines):
            if i < j and isOverlapped(l1, l2):
                return False

    return True

def dfs(level):
    global res
    if level == n:
        if isPossible():
            res = max(res, len(selected_lines))
        return
    
    selected_lines.append(lines[level])
    dfs(level + 1)
    selected_lines.pop()

    dfs(level + 1)

dfs(0)
print(res)