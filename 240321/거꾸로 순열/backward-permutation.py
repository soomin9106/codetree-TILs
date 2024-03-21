n = int(input())

answer = []
visited = [False] * (n+1)

def print_answer():
    for a in answer:
        print(a, end = ' ')
    print()

def dfs(cur_num):
    if cur_num == n:
        print_answer()
        return 

    for i in range(n, 0, -1):
        if visited[i]:
            continue

        visited[i] = True
        answer.append(i)

        dfs(cur_num + 1)

        answer.pop()
        visited[i] = False

dfs(0)