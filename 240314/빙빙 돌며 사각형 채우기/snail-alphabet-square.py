# 65 - 90 chr(숫자)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

n, m = map(int, input().split())

arr = [[''] * m for _ in range(n)]

dx = [0, 1, 0, -1]  
dy = [1, 0, -1, 0]

x, y = 0, 0
direction = 0  
arr[0][0] = 'A'
for i in range(1, n * m):  # 총 칸 수만큼 반복
    nx, ny = x + dx[direction], y + dy[direction]
    
    if in_range(nx, ny) and arr[nx][ny] == '':
        x, y = nx, ny
        arr[x][y] = chr(ord('A') + i % 26)
    else:
        direction = (direction + 1) % 4
        x, y = x + dx[direction], y + dy[direction]
        arr[x][y] = chr(ord('A') + i % 26)  
        


# 결과 출력
for row in arr:
    print(' '.join(row))