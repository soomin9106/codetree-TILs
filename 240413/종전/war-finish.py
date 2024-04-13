n = int(input())

INT_MAX = int(1e9)

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

border = [
    [False] * n
    for _ in range(n)
]

total_sum = sum([
    grid[i][j]
    for i in range(n)
    for j in range(n)
])

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def possible_to_draw(x, y, k, l):
    return in_range(x - k, y + k) and in_range(x - k - l, y + k - l) and \
            in_range(x - l, y - l)

def draw_border(x, y, k, l):
    move_nums = [k, l, k, l]
    # 1,2,3,4 방향대로
    dxs = [-1, -1, 1, 1]
    dys = [1, -1, -1, 1]

    # 경계선 초기화
    for i in range(n):
        for j in range(n):
            border[i][j] = False

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy
            border[x][y] = True

def get_score(x, y, k, l):
    population = [0, 0, 0, 0, 0]
    draw_border(x, y, k, l)

    # 좌측 상단
    for i in range(x - l):
        for j in range(y + k - l + 1):
            if border[i][j]:
                break
            
            population[0] += grid[i][j]

    # 좌측 하단
    for i in range(x - l, n):
        for j in range(y):
            if border[i][j]:
                break

            population[1] += grid[i][j]

    # 우측 상단
    for i in range(x - k + 1):
        for j in range(n - 1, y + k - l, -1):
            if border[i][j]:
                break

            population[2] += grid[i][j]

    # 우측 하단 구역
    for i in range(x - k + 1, n):
        for j in range(n - 1, y - 1, -1):
            if border[i][j]:
                break
            population[3] += grid[i][j]

    # 중간 영역
    population[4] = total_sum - sum(population[:4])

    return max(population) - min(population)

ans = INT_MAX

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                if possible_to_draw(i, j, k, l):
                    ans = min(ans, get_score(i, j, k, l))

print(ans)