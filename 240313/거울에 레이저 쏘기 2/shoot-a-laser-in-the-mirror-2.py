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

# 출발점에 따라 다르게
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
while in_range(x, y):
    # print(x, y)
    cnt += 1
    if maps[x][y] == '/':
        if d == 3:
            d = 2
        elif d == 2: 
            d = 3
        elif d == 0:
            d = 1
        else:
            d = 0
        
    else:
        if d == 0:
            d = 3
        elif d == 3:
            d = 0
        elif d== 1:
            d = 2
        else:
            d = 1
        
    
    x, y = x + dxs[d], y + dys[d]
        

print(cnt)