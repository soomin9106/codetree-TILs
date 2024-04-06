from collections import deque

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

next_arr = [
    [0] * n
    for _ in range(n)
]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

visited = [[0] * n for _ in range(n)]
group_cnt = [0]

# 하나의 이차원 리스트 그룹핑 (1번 ~)
def grouping(x, y, group_num):
    q = deque()
    q.append((x, y))
    visited[x][y] = group_num
    cnt = 1

    while q:
        cur_x, cur_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny) and arr[nx][ny] == arr[cur_x][cur_y] and visited[nx][ny] == 0:
                visited[nx][ny] = group_num
                q.append((nx, ny))
                cnt += 1

    return cnt

# 예술성 점수 구하기
def get_art_score():
    art_score = 0

    for i in range(n):
        for j in range(n):
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy

                if in_range(nx, ny) and arr[i][j] != arr[nx][ny]:
                    val1, val2 = arr[i][j], arr[nx][ny]
                    gcnt1, gcnt2 = group_cnt[visited[i][j]], group_cnt[visited[nx][ny]]

                    art_score += (gcnt1 + gcnt2) * val1 * val2

    return art_score // 2



def rotate_square(i1, j1):
    mid = n // 2

    for x in range(i1, i1 + mid):
        for y in range(j1, j1 + mid):
            ox, oy = x - i1, y -j1

            rx, ry = oy, mid - ox - 1

            next_arr[rx + i1][ry + j1] = arr[x][y]

# 회전 시키기
def rotate():
    mid = n // 2

    for i in range(n):
        for j in range(n):
            next_arr[i][j] = 0


    for i in range(n):
        for j in range(n):
            # Case 2 - 1. 세로줄에 대해서는 (i, j) -> (j, i)가 됩니다.
            if j == n // 2:
                next_arr[j][i] = arr[i][j]
            # Case 2 - 2. 가로줄에 대해서는 (i, j) -> (n - j - 1, i)가 됩니다.
            elif i == n // 2:
                next_arr[n - j - 1][i] = arr[i][j]

    rotate_square(0, 0)
    rotate_square(mid + 1, 0)
    rotate_square(0, mid + 1)
    rotate_square(mid + 1, mid + 1)

    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]


# 한번의 예술성 점수 검사
def simulate():
    global visited, group_cnt
    # grouping
    visited = [[0] * n for _ in range(n)]
    group_cnt = [0]
    group_num = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                cnt = grouping(i, j, group_num)
                group_num += 1
                group_cnt.append(cnt)


    score = get_art_score()

    return score


    
art_scores = 0
for _ in range(4):
    score = simulate()
    # print(score)
    art_scores += score

    rotate()

print(art_scores)