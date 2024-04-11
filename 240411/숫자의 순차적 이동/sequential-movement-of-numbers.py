n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def swap(r, c):
    # 8 개의 방향
    dxs = [1, -1, 0, 0, 1, 1, -1, -1]
    dys = [0, 0, 1, -1, 1, -1, 1, -1]

    max_val = 0
    max_x, max_y = -1, -1

    for dx, dy in zip(dxs, dys):
        nx, ny = r + dx, c + dy

        if in_range(nx, ny) and arr[nx][ny] > max_val:
            max_val = arr[nx][ny]
            max_x, max_y = nx, ny

    temp = arr[r][c]
    arr[r][c] = max_val
    arr[max_x][max_y] = temp

def turn():
    for i in range(1, n * n + 1):
    # i 숫자에 대한 액션
        curx, cury = -1, -1
        for r in range(n):
            for c in range(n):
                if arr[r][c] == i:
                    curx, cury = r, c
                    break

        swap(curx, cury)
                    
                    

for _ in range(m):
    turn()

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()