n, k = map(int, input().split())

arr = []
arr.append([0 for _ in range(n + 1)])
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

prefix_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + arr[i][j]

def get_sum(s1, e1, s2, e2):
    return prefix_sum[s2][e2] - prefix_sum[s1 - 1][e2] - prefix_sum[s2][e1 - 1] + prefix_sum[s1 - 1][e1 - 1]

def in_range(x, y):
    return 0 < x < n + 1 and 0 < y < n + 1

answer = -int(1e9)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if in_range(i+k-1, j+k-1):
            answer = max(answer, get_sum(i, j, i + k-1, j + k-1))

print(answer)