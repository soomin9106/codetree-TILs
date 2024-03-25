n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

r, c = map(int, input().split())
x = r - 1
y =  c - 1

val = arr[x][y]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for dx, dy in zip(dxs, dys):
    cur_x, cur_y = x, y
    for _ in range(val - 1):
        nx, ny = cur_x + dx, cur_y + dy

        if in_range(nx, ny):
            arr[nx][ny] = 0
            cur_x, cur_y = nx, ny

arr[x][y] = 0

def change_val(col_arr):
    if 0 not in col_arr:
        return col_arr
    
    temp = []
    temp_idx = 0

    for i in range(len(col_arr)):
        if col_arr[i] != 0:
            temp.append(col_arr[i])
            temp_idx += 1

    for j in range(len(col_arr) - temp_idx):
        temp.insert(0, 0)

    return temp

# 열별로 중력 이동 실행
for j in range(n):
    col_arr = []
    for i in range(n):
        col_arr.append(arr[i][j])
    
    new_arr = change_val(col_arr)
    # print(new_arr)

    for i in range(n):
        arr[i][j] = new_arr[i]
    
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()