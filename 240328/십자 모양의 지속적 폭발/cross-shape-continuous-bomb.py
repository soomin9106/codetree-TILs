n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bomb(arr, col):

    new_arr = [[0] * n for _ in range(n)]
    row = 0

    for i in range(len(arr)):
        if arr[i][col] != 0:
            row = i
            break

    repeat = arr[row][col]

    cur_x, cur_y = row, col
    arr[cur_x][cur_y] = 0
    for dx, dy in zip(dxs, dys):

        for i in range(1, repeat):
            nx, ny = cur_x + (dx * i), cur_y + (dy * i)
            if in_range(nx, ny):
                arr[nx][ny] = 0

    for j in range(n):
        temp = []
        for i in range(n):
            if arr[i][j] != 0:
                temp.append(arr[i][j])

        for _ in range(n - len(temp)):
            temp.insert(0, 0)
        
        for i in range(n):
            new_arr[i][j] = temp[i]
    return new_arr
    
for _ in range(m):
    c = int(input())
    c -= 1

    arr = bomb(arr, c)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()