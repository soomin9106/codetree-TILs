n = int(input())

arr = []
arr.append([0] * (n + 1))
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + \
                            prefix_sum[i][j-1] - \
                            prefix_sum[i-1][j-1] + \
                            arr[i][j]

def in_range(x, y):
    return 0 < x < n + 1 and 0 < y < n + 1

def get_sum(s1, e1, s2, e2):
    return prefix_sum[s2][e2] - \
                prefix_sum[s1 - 1][e2] - \
                prefix_sum[s2][e1 - 1] + \
                prefix_sum[s1 - 1][e1 - 1]

# 시작행 r1, 끝 행 r2
def get_max_rect(r1, r2):
    dp = [0] * (n + 1)

    for y in range(1, n + 1):
        val = get_sum(r1, y, r2, y)
        dp[y] = max(val, dp[y - 1] + val)

    max_area = -int(1e9)
    for y in range(1, n + 1):
        max_area = max(max_area, dp[y])

    return max_area
    

answer = -int(1e9)
for i in range(1, n + 1):
    for j in range(i, n + 1):
        answer = max(answer, get_max_rect(i, j))

print(answer)