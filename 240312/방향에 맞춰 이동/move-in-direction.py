n = int(input())
x, y = 0, 0

arr = []

for _ in range(n):
    direction, cost = map(str, input().split())
    arr.append((direction, int(cost)))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    direction, cost = arr[i]

    if direction == 'N':
        for _ in range(cost):
            x += dx[3]
            y += dy[3]
    if direction == 'E':
        for _ in range(cost):
            x += dx[1]
            y += dy[1]
    if direction == 'S':
        for _ in range(cost):
            x += dx[2]
            y += dy[2]
    if direction == 'W':
        for _ in range(cost):
            x += dx[0]
            y += dy[0]

    # print(x, y)

print(x, y)