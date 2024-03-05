import sys

n, m = map(int, input().split())
str_map = []

for i in range(n):
    row = []
    s = input()
    for j in range(m):
        row.append(s[j])
    str_map.append(row)

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

res = 0
for i in range(n):
    for j in range(m):
        if str_map[i][j] == "L":
            for k in range(8):
                nx, ny = i + dx[k], j + dy[k]
                count = 0
                while 0 <= nx < n and 0 <= ny < m and str_map[nx][ny] == "E" and count < 2:
                    count += 1
                    nx, ny = nx + dx[k], ny + dy[k]
                if count == 2:
                    res += 1

print(res)