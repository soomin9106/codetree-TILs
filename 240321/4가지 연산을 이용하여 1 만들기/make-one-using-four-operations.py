n = int(input())

# 연산 종류
calcs = [0, 1, 2, 3]

def possible(num, i):
    if i == 0:
        return True
    elif i == 1:
        return True
    elif i == 2 and num % 2 == 0:
        return True
    elif i == 3 and num % 3 == 0:
        return True
    return False

def calculate(num, i):
    if i == 0:
        return num - 1
    if i == 1:
        return num + 1
    if i == 2:
        return num / 2
    if i == 3:
        return num / 3

ans = int(1e9)
def dfs(num, cnt):
    global ans
    if num == 1:
        ans = min(ans, cnt)
        return 
    
    if cnt >= n - 1:
        return 

    for i in range(4):
        if possible(num, i):
            dfs(calculate(num, i), cnt + 1)


dfs(n, 0)
print(ans)