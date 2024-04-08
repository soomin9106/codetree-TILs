n = int(input())

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

arr = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def choose_seat(n0, n1, n2, n3, n4):
    candidates = []
    
    for i in range(n):
        for j in range(n):
            likes_cnt = 0
            blank_cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy

                if in_range(nx, ny) and arr[nx][ny] in [n1, n2, n3, n4]:
                    likes_cnt += 1
                elif in_range(nx, ny) and arr[nx][ny] == 0:
                    blank_cnt += 1
            
            candidates.append([likes_cnt, blank_cnt, i, j])

    
    sorted_candidates = sorted(candidates, key = lambda x: (-x[0], -x[1], x[2], x[3]))

    # print(sorted_candidates)
    res_x, res_y = sorted_candidates[0][2], sorted_candidates[0][3]

    for i in range(0, len(sorted_candidates) - 1):
        curx, cury = sorted_candidates[i][2], sorted_candidates[i][3]
        if arr[curx][cury] != 0:
            res_x, res_y = sorted_candidates[i + 1][2], sorted_candidates[i + 1][3]
        else:
            break

    return res_x, res_y

infos = {}

for _ in range(n * n):
    n0, n1, n2, n3, n4 = map(int, input().split())
    infos[n0] = [n1, n2, n3, n4]
    x, y = choose_seat(n0, n1, n2, n3, n4)

    arr[x][y] = n0


scores = [0, 1, 10, 100, 1000]
answer = 0
for i in range(n):
    for j in range(n):
        like_cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy

            if in_range(nx, ny) and arr[nx][ny] in infos[arr[i][j]]:
                like_cnt += 1

        answer += scores[like_cnt]

print(answer)