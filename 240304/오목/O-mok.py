import sys

games = []

for _ in range(19):
    games.append(list(map(int, input().split())))

cnt = 0
val = 0

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def check_winner(x, y):
    point_lst = []
    for k in range(8):
        cnt = 1
        nx, ny = x + dx[k], y + dy[k]
        while 0 <= nx < 19 and 0 <= ny < 19 and games[nx][ny] == games[x][y]:
            cnt += 1
            nx, ny = nx + dx[k], ny + dy[k]

        if cnt == 5:
            # print(point_lst)
            return games[x][y], [x + (2 * dx[k]), y + (2 * dy[k])]

    return 0, point_lst

for i in range(19):
    for j in range(19):
        if games[i][j] == 1 or games[i][j] == 2:
            result, point_lst = check_winner(i, j)
            if result != 0:
                print(result)
                print('{} {}'.format(point_lst[0] + 1, point_lst[1] + 1))
                sys.exit()

print(0)