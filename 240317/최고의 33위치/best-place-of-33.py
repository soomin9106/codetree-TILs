n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))


def calc(i, j):
    cnt = 0
    for k in range(i, i + 3):
        for l in range(j, j+ 3):
            if arr[k][l] == 1:
                cnt += 1
    return cnt


res = 0
for i in range(0, n - 2):
    for j in range(0, n - 2):
        res = max(res, calc(i, j))

print(res)