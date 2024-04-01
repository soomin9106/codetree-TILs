n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def init_temp():
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp[i][j] = arr[i][j]

    return temp

def bomb(x, y):
    temp = init_temp()
    val = temp[x][y]
    temp[x][y] = 0 

    for dx, dy in zip(dxs, dys):
        cur_x, cur_y = x, y
        for i in range(val - 1):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny):
                temp[nx][ny] = 0
                cur_x, cur_y = nx, ny

    new_arr = []

    for j in range(n):
        new_col = []

        for i in range(n):
            if temp[i][j] != 0:
                new_col.append(temp[i][j])
        
        for _ in range(n - len(new_col)):
            new_col.insert(0, 0)
        
        new_arr.append(new_col)

    res = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            res[i][j] = new_arr[j][i]

    return res

def count(row):
    cnt = 0
    for i in range(len(row) - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            cnt += 1
    return cnt


def calc(res_arr):
    cnt = 0
    for i in range(n):
        row = res_arr[i]
        cnt += count(row)

    for j in range(n):
        row = []
        for i in range(n):
            row.append(res_arr[i][j])
        cnt += count(row)

    return cnt 
        


answer = -int(1e9)
for i in range(n):
    for j in range(n):
        res_arr = bomb(i, j)
        # answer = max(answer, calc(res_arr))
        val = calc(res_arr)
        if answer < val:
            # print(res_arr, val)
            answer = val

print(answer)