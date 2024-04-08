n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited_pos = []
max_sum = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and (x, y) not in visited_pos

def get_max_sum(cnt, sum_of_nums):
    if cnt == 4:
        global max_sum
        max_sum = max(max_sum, sum_of_nums)
        return 

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for (x, y) in visited_pos:
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                visited_pos.append((nx, ny))
                get_max_sum(cnt + 1, sum_of_nums + arr[nx][ny])
                visited_pos.pop()

    return

for i in range(n):
    for j in range(m):
        visited_pos.append((i, j))
        get_max_sum(1, arr[i][j])
        visited_pos.pop()

print(max_sum)