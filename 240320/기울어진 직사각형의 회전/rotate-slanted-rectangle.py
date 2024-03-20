n = int(input())
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

r, c, m1, m2, m3, m4, direction = map(int, input().split())
r -= 1
c -= 1

temp = [[0] * n for _ in range(n)]

def shift(x, y, k, l, move_dir):
    if move_dir == 0:
        dxs = [-1, -1, 1, 1]
        dys = [1, -1, -1, 1]
        move_nums = [k, l, k, l]

    else:
        dxs = [-1, -1, 1, 1]
        dys = [-1, 1, 1, -1]
        move_nums = [l, k, l, k]

    
    # temp 배열에 grid 값 복사 
    for i in range(n):
        for j in range(n):
            temp[i][j] = grid[i][j]

    # 기울어진 직사각형 경계 따라가기
    # 숫자를 한칸씩 밀기
    # temp 에 저장

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            nx, ny = x + dx, y + dy
            temp[nx][ny] = grid[x][y]
            x, y = nx, ny

    # temp -> grid
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]

shift(r, c, m1, m2, direction)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()