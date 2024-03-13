# \ => 오른쪽으로 꺾기
# / => 왼쪽으로 꺾기

# 1 ~ n => 위에서 내려옴
# n+1 ~ 2n => 오른쪽에서 들어옴
# 2n + 1 ~ 3n => 아래에서 내려옴
# 3n + 1 ~ 4n => 왼쪽에서 들어옴

n = int(input())
maps = [input() for _ in range(n)]


k = int(input())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 처음 direction 선택 & 위치 설정
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

d = 0
x, y = 0, 0

# 여기 인덱스 잘 정해보는걸로...
if 1 <= k <= n:
    d = 0
    x, y = 0, k - 1
if n + 1 <= k <= 2*n:
    d = 1
    x, y = k - n - 1, n - 1
if 2*n + 1 <= k <=3*n:
    d = 2
    x, y = n - 1, n - (k - n*2)
if 3*n + 1 <= k <= 4*n :
    d = 3
    x, y = n - (k - n*3), 0

# print(maps)
cnt = 0
while True:
    # print(x, y)
    cnt += 1
    if maps[x][y] == '/':
        if d == 3:
            d = 2
        if d == 2: 
            d = 3
        if d == 0:
            d = 1
        if d == 1:
            d = 0
        
    else:
        if d == 0:
            d = 3
        if d == 3:
            d = 0
        if d== 1:
            d = 2
        if d == 2:
            d = 1
        
    nx, ny = x + dxs[d], y + dys[d]
    if not in_range(nx, ny):
        break
    x, y = nx, ny
        

print(cnt)