from collections import deque

n, m = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def calc_cost(i, j, k):
    q = deque()
    q.append((i, j))
    map_cnt = (k * k) + ((k + 1) * (k + 1))
    k_cnt = 0
    gold_cnt = 1 if maps[i][j] == 1 else 0

    while q and k_cnt < k:
        cur_x, cur_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if not in_range(nx, ny):
                continue
            elif maps[nx][ny] == 1:
                gold_cnt += 1
            # 무조건 다음 스탭을 위해서 넣어야 함
            q.append((nx, ny))
        
        k_cnt += 1

    # print(gold_cnt, map_cnt)
    return (m * gold_cnt) - map_cnt, gold_cnt # cost, count 순으로 반환


max_change_cnt = 0
number_k = 0
count_res = 0

while True:
    for i in range(n):
        for j in range(n):
            cost, count = calc_cost(i, j, number_k)
            if cost > 0: # 손해보지 않을 때
                max_change_cnt += 1
                count_res = max(count_res, count)

    if max_change_cnt <= 0:
        break
    number_k += 1
    max_change_cnt = 0

print(count_res)