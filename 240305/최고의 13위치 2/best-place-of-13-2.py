import sys

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

res = -int(1e9)

for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):
                if i == k and abs(j - l) <= 2:
                    continue
                else:
                    res = max(res, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[k][l] + arr[k][l+1] + arr[k][l+2])
print(res)