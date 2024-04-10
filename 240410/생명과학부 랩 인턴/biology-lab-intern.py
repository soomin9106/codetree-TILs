n, m, k = map(int, input().split())

# (곰팡이 방향, 곰팡이 크기, 곰팡이 속력) => (0, 0, 0) 인 경우는 곰팡이가 없는 경우 
mold_maps = [[[0, 0, 0]] * m for _ in range(n)]

for _ in range(k):
    x, y, s, d, b = map(int, input().split())
    x -= 1
    y -= 1

    mold_maps[x][y] = [d, b, s]

# 1,2,3,4 => 위, 아래, 오른쪽, 왼쪽
dxs = [0, -1, 1, 0, 0]
dys = [0, 0, 0, 1, -1]

def convert_d(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    else:
        return 3

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 제일 빨리 발견된 곰팡이를 채취
def get_mold(order, col):
    ans = 0
    for idx, (d, b, s) in enumerate(col):
        if d != 0 and b != 0:
            ans = b
            mold_maps[idx][order] = [0, 0, 0]
            break

    return ans

def initialize_molds():
    for i in range(n):
        for j in range(m):
            mold_maps[i][j] = [0, 0, 0]

#곰팡이의 이동
def move():
    move_res = []
    for i in range(n):
        for j in range(m):
            curd, curb, curs = mold_maps[i][j]

            if curd != 0 and curb != 0: # 곰팡이인 경우
                curi, curj = i, j
                for _ in range(curs):
                    ni, nj = curi + dxs[curd], curj + dys[curd]

                    if in_range(ni, nj):
                        curi, curj = ni, nj
                    else:
                        curd = convert_d(curd)
                        ni, nj = curi + dxs[curd], curj + dys[curd]
                        curi, curj = ni, nj
                
                move_res.append((curi, curj, curd, curb, curs))

    initialize_molds()
    for (curi, curj, curd, curb, curs) in move_res:
        # print(move_res)
        d, b, s = mold_maps[curi][curj]

        if curb > b:
            mold_maps[curi][curj] = [curd, curb, curs]

    # print('moldmaps', mold_maps)
    # print()


# 입력 예시: [[0, 0, 0], [3, 3, 5], [0, 0, 0], [0, 0, 0], [4, 5, 1]]
def inspect(order, col):
    getted = get_mold(order, col)

    move()

    return getted

answer = 0
for j in range(m):
    getted = inspect(j, [mold[j] for mold in mold_maps])
    answer += getted

print(answer)