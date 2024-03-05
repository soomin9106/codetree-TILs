import sys
k, n = map(int, input().split())

answer = []

def print_answer():
    for i in range(n):
        print(answer[i], end = ' ')
    print()

def dfs(level):
    global answer
    if level == n:
        print_answer()
        return

    for i in range(1, k + 1):
        answer.append(i)
        dfs(level+1)
        answer.pop()


dfs(0)