n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dxs = [1, -1, 0 , 0]
dys = [0, 0, -1, 1]

res = 0

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if inRange(nx, ny) and arr[nx][ny] == 1:
                cnt += 1

        if cnt >= 3:
            res += 1

print(res)