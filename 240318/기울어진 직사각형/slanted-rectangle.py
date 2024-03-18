from collections import deque

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

# 1, 2, 3, 4 방향대로
dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def do_simulate(x, y, length, direction):
    temp_cost = arr[x][y]
    cur_x, cur_y = x, y
    for _ in range(length - 1):
        temp_x, temp_y = cur_x + dxs[direction], cur_y + dys[direction]  # 수정된 부분

        if not in_range(temp_x, temp_y):
            cur_x, cur_y = temp_x, temp_y
            break
        else:
            cur_x, cur_y = temp_x, temp_y
            temp_cost += arr[cur_x][cur_y]

    return temp_cost, cur_x, cur_y


# 너비, 높이, 시작 지점 고정
def calc_cost(width, height, x, y):
    cur_x, cur_y = x, y
    cost = 0
    temp_cost, cur_x, cur_y = do_simulate(cur_x, cur_y, width, 0)
    # print(x, y, temp_cost, cur_x, cur_y)

    if not in_range(cur_x, cur_y):
        return 0
    else:
        temp_cost -= arr[cur_x][cur_y]
        cost += temp_cost
    
    temp_cost, cur_x, cur_y = do_simulate(cur_x, cur_y, height, 1)
    # print(x, y, temp_cost, cur_x, cur_y)

    if not in_range(cur_x, cur_y):
        return 0
    else:
        temp_cost -= arr[cur_x][cur_y]
        cost += temp_cost

    temp_cost, cur_x, cur_y = do_simulate(cur_x, cur_y, width, 2)
    # print(x, y, temp_cost, cur_x, cur_y)

    if not in_range(cur_x, cur_y):
        return 0
    else:
        temp_cost -= arr[cur_x][cur_y]
        cost += temp_cost

    temp_cost, cur_x, cur_y = do_simulate(cur_x, cur_y, height, 3)
    # print(x, y, temp_cost, cur_x, cur_y)

    if not in_range(cur_x, cur_y):
        return 0
    else:
        temp_cost -= arr[cur_x][cur_y]
        cost += temp_cost

    return cost

    
    

            

# 가로 길이 기준으로 For 문 돌기
result = 0
for width in range(1, n):
    for height in range(1, n):  
        for x in range(n):
            for y in range(n):
                result = max(result, calc_cost(width, height, x, y))

# example
# calc_cost(4, 2, 4, 1)

print(result)