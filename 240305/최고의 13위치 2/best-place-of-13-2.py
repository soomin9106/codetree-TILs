import sys

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

res_list = []

for i in range(n):
    for j in range(n - 2):
        res_list.append((arr[i][j] + arr[i][j+1] + arr[i][j+2], i, j))

res_list = sorted(res_list, key = lambda x: -x[0])

print(res_list[0][0] + res_list[1][0])