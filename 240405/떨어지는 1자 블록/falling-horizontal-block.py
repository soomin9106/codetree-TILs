n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

k -= 1
cur_row = 0

for i in range(n):
    if sum(arr[i][k: k+m]) == 0:
        cur_row = i
    else:
        break

for j in range(k, k + m):
    arr[cur_row][j] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()