from collections import deque

n, m, q = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
temp = [[0]*m for _ in range(n)]
winds = []

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    winds.append((r1-1, c1-1, r2-1, c2-1))

def rotate(r1, c1, r2, c2):
    u_row = arr[r1][c1:c2]
    d_row = arr[r2][c1+1:c2+1]

    r_col=[
        arr[r][c2]
        for r in range(r1, r2)
    ]

    l_col=[
        arr[r][c1]
        for r in range(r1+1, r2+1)
    ]

    # print(u_row)
    # print(d_row)
    # print(r_col)
    # print(l_col)

    u_row.insert(0, l_col[0])
    arr[r1][c1: c2 + 1] = u_row

    idx = 0
    for rr in range(r1+1, r2+1):
        arr[rr][c2] = r_col[idx]
        idx += 1

    arr[r2][c1: c2] = d_row

    idx = 0
    for rr in range(r1, r2):
        arr[rr][c1] = l_col[idx]
        idx += 1

    # for i in range(n):
    #     for j in range(m):
    #         print(arr[i][j], end = ' ')
    #     print()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def calc(i, j):
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]

    count = 1
    total = arr[i][j]

    for dx, dy in zip(dxs, dys):
        nx, ny = i + dx, j + dy

        if in_range(nx, ny):
            count += 1
            total += arr[nx][ny]

    return total // count

def change_val(r1, c1, r2, c2):
    for i in range(r1, r2 +1):
        for j in range(c1, c2 + 1):
            res = calc(i, j)
            temp[i][j] = res

    for i in range(r1, r2 +1):
        for j in range(c1, c2 + 1):
            arr[i][j] = temp[i][j]



def do_simulate(r1, c1, r2, c2):
    rotate(r1, c1, r2, c2)

    change_val(r1, c1, r2, c2)


for wind in winds:
    r1, c1, r2, c2 = wind
    do_simulate(r1, c1, r2, c2)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()