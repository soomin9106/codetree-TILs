n = int(input())

arr = []
for _ in range(n):
    temp = []
    row = input()
    for i in range(n):
        temp.append(row[i])
    arr.append(temp)

def is_digit(num):
    if num.isdigit():
        return int(num)
    else:
        return -1

# coin 위치들 리스트 만들어 주기
coins = []
def make_coin_list(): # (coin_number, (coin_x, coin_y))
    global coins
    for i in range(n):
        for j in range(n):
            num = is_digit(arr[i][j]) 
            if num >= 0:
                coins.append((num, (i, j)))

make_coin_list()
coins.sort()

# 시작점과 끝점 리스트 만들어주기 
start_end = []
def make_start_end_list():
    global start_end
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'S':
                start_end.append((0, (i, j)))
            elif arr[i][j] == 'E':
                start_end.append((11, (i, j)))

make_start_end_list()
start_end.sort()

ans = int(1e9)
selected_coords = []
def make_coin_combination(curr_idx, cnt):
    global ans, selected_coords
    if cnt == 3:
        ans = min(calc_coords(), ans)
        return
    
    if curr_idx == len(coins):
        return 
    
    make_coin_combination(curr_idx + 1, cnt)

    selected_coords.append(coins[curr_idx])
    make_coin_combination(curr_idx + 1, cnt +1)
    selected_coords.pop()

# 좌표 사이 거리를 가져오는 함수
def get_dt(coord1, coord2):
    r1, c1 = coord1
    r2, c2 = coord2
    return abs(r1 - r2) + abs(c1 - c2)

def calc_coords():
    # 거리 계산하는 함수
    coords = []
    coords.append(start_end[0][1])
    for c in selected_coords:
        coords.append(c[1])
    coords.append(start_end[1][1])

    move_dt = 0
    for idx in range(4):
        move_dt += get_dt(coords[idx], coords[idx + 1])

    return move_dt

make_coin_combination(0, 0)
if ans == int(1e9):
    print(-1)
    exit(0)
print(ans)