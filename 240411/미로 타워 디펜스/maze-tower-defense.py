n, m = map(int, input().split())

# → ↓ ← ↑
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

commands = []
for _ in range(m):
    d, p = map(int, input().split())
    commands.append((d, p))

new_maps = [
    [0] * n 
    for _ in range(n)
]


def print_maps():
    for i in range(n):
        for j in range(n):
            print(maps[i][j], end = ' ')
        print()

    print()

# 중앙 격자 인덱스
mid = n // 2 

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 달팽이 모양의 격자들을 순서대로 관리
locations = []
def make_location():
    global locations
    # 하우상좌 순서 (달팽이 이동)
    move_dxs, move_dys = [1, 0, -1, 0], [0, 1, 0, -1]
    move_num, move_dir = 1, 0

    x, y = mid, mid - 1
    locations.append((x, y))

    while True:
        for _ in range(move_num):
            nx, ny = x + move_dxs[move_dir], y + move_dys[move_dir]

            if (nx, ny) == (0, -1):
                return
            x, y = nx, ny
            locations.append((x, y))
        
        if move_dir == 0 or move_dir == 2:
            move_num += 1
        
        move_dir = (move_dir + 1) % 4

make_location()

def initialize_new_maps():
    for i in range(n):
        for j in range(n):
            new_maps[i][j] = 0

# 1. 플레이어는 상하좌우 방향 중 주어진 공격 칸 수만큼 몬스터를 공격하여 없앨 수 있습니다.
def attack(d, p):
    x, y = mid, mid
    s = 0

    for _ in range(p):
        nx, ny = x + dxs[d], y + dys[d]

        x, y = nx, ny
        s += maps[x][y]
        maps[x][y] = 0

    return s

# 2. 비어있는 공간만큼 몬스터는 앞으로 이동하여 빈 공간을 채웁니다.
def fill():
    initialize_new_maps()
    numbers = []
    
    # 0 을 제외한 숫자들을 채워 줌 
    for (x, y) in locations:
        if maps[x][y] != 0:
            numbers.append(maps[x][y])

    for i in range(len(numbers)):
        if i >= n * n - 1:
            break
        x, y = locations[i]
        new_maps[x][y] = numbers[i]

    # new_maps 의 내용을 maps 에 복사
    for i in range(n):
        for j in range(n):
            maps[i][j] = new_maps[i][j]

# 3. 이때 몬스터의 종류가 4번 이상 반복하여 나오면 해당 몬스터 또한 삭제됩니다. 해당 몬스터들은 동시에 사라집니다.

# 몬스터 종류가 4번 이상 나오는지 확인 + 그 위치들 구하기
# 반환된 위치 기반으로 fill 다시 수행
def get_continue_loc():
    continues = []
    cur_x, cur_y = mid, mid - 1
    cur_val = maps[cur_x][cur_y]
    temp_con = [(cur_x, cur_y)]

    for idx, (x, y) in enumerate(locations):
        if idx == 0:
            continue
        if maps[x][y] == cur_val:
            temp_con.append((x, y))
        else:
            if len(temp_con) >= 4:
                # print('appended', temp_con)
                continues.append(temp_con)
            temp_con = []
            temp_con.append((x, y))
            cur_val = maps[x][y]

    return continues
    
def refill(continues):
    s = 0
    for item in continues:
        for (x, y) in item:
            s += maps[x][y]
            maps[x][y] = 0

    fill()

    return s

# 4. 삭제가 끝난 다음에는 몬스터를 차례대로 나열했을 때 같은 숫자끼리 짝을 지어줍니다. 
# 이후 각각의 짝을 (총 개수, 숫자의 크기)로 바꾸어서 다시 미로 속에 집어넣습니다.
def make_new_row():
    numbers = []

    for (x, y) in locations:
        if maps[x][y] == 0:
            break
        numbers.append(maps[x][y])

    # print(numbers)

    return numbers

def fill_with_count():
    numbers = make_new_row()
    new_row = []

    # print('numbers', numbers)

    cur_num = numbers[0]
    cur_cnt = 1
    idx = 1

    while idx < len(numbers):
        if cur_num == numbers[idx]:
            cur_cnt += 1
        else:
            new_row.append(cur_cnt)
            new_row.append(cur_num)

            cur_num = numbers[idx]
            cur_cnt = 1

        idx += 1

    new_row.append(cur_cnt)
    new_row.append(cur_num)

    initialize_new_maps()
    for i in range(len(new_row)):
        if i >= n * n - 1:
            break
        x, y = locations[i]

        new_maps[x][y] = new_row[i]

    # new_maps 의 내용을 maps 에 복사
    for i in range(n):
        for j in range(n):
            maps[i][j] = new_maps[i][j]

score =  0  
for (d, p) in commands:
    score += attack(d, p)
    fill()

    while True:
        # print_maps()
        continues = get_continue_loc()

        if len(continues) == 0:
            break
        else:
            score += refill(continues)

    fill_with_count()


print(score)