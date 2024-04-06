n = int(input())
arr = list(map(int , input().split()))

op = list(map(int , input().split()))

min_ans = int(1e9)
max_ans = -int(1e9)

operators = []
for idx, o in enumerate(op):
    val = ''
    if idx == 0:
        val = '+'

    elif idx == 1:
        val = '-'
    else:
        val = '*'

    for _ in range(o):
        operators.append(val)


visited = [False] * (n - 1)
def dfs(cur_arr):
    global min_ans, max_ans
    if len(cur_arr) == n - 1:
        val = arr[0]
        op_idx = 0
        for i in range(1, len(arr)):
            if cur_arr[op_idx] == '+':
                val += arr[i]
            elif cur_arr[op_idx] == '-':
                val -= arr[i]
            else:
                val *= arr[i]
            op_idx += 1
        
        min_ans = min(min_ans, val)
        max_ans = max(max_ans, val)
        return 

    for i in range(len(operators)):
        if not visited[i]:
            visited[i] = True
            dfs(cur_arr + [operators[i]])
            visited[i] = False


dfs([])
print(min_ans, max_ans)