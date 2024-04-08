from collections import defaultdict

n, m, k = map(int, input().split())

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

arr = defaultdict(list)

# 이동하는 함수
def move(x, y, curm, curs, curd):
    for _ in range(curs):
        nx, ny = x + dxs[curd], y + dys[curd]

        if nx >= n:
            nx = 0
        if ny >= n:
            ny = 0
        if nx < 0:
            nx = n -1
        if ny < 0:
            ny = n - 1
        
        x, y = nx, ny

    return x, y, curm, curs, curd

points = []
for _ in range(m):
    x, y, curm, curs, curd = map(int, input().split())
    x -= 1
    y -= 1

    arr[(x, y)].append([curm, curs, curd])

def calc(cur_arr):
    res_arr = defaultdict(list)

    for key in cur_arr:
        if len(cur_arr[key]) <= 1:
            res_arr[key] = cur_arr[key]
        else:
            sum_m = 0
            sum_s = 0
            new_d = 'UP'

            for (curm, curs, curd) in cur_arr[key]:
                sum_m += curm
                sum_s += curs

                if curd not in [0, 2, 4, 6]:
                    new_d = 'TRI'

            if sum_m // 5 == 0:
                continue
            
            if new_d == 'UP':
                res_arr[key].append([sum_m // 5, sum_s // len(cur_arr[key]), 0])
                res_arr[key].append([sum_m // 5, sum_s // len(cur_arr[key]), 2])
                res_arr[key].append([sum_m // 5, sum_s // len(cur_arr[key]), 4])
                res_arr[key].append([sum_m // 5, sum_s // len(cur_arr[key]), 6])
            else:
                res_arr[key].append([sum_m // 5, sum_s // len(cur_arr[key]), 1])
                res_arr[key].append([sum_m // 5, sum_s // len(cur_arr[key]), 3])
                res_arr[key].append([sum_m // 5, sum_s // len(cur_arr[key]), 5])
                res_arr[key].append([sum_m // 5, sum_s // len(cur_arr[key]), 7])

    return res_arr


def calc_sum(cur_arr):
    res = 0
    for key in cur_arr:
        for (curm, _, _) in cur_arr[key]:
            res += curm

    return res


def simulate():
    global arr
    new_arr = defaultdict(list)
    for x, y in arr:
        for idx, items in enumerate(arr[(x, y)]):
            curm, curs, curd = items
            nextx, nexty, nextm, nexts, nextd = move(x, y, curm, curs, curd) 
            new_arr[(nextx, nexty)].append([nextm, nexts, nextd])

    arr = new_arr
    
    # 원자 충돌 시 합성
    arr = calc(arr)

    # print(arr)

    res = calc_sum(arr)
    
    return res

    
ans = 0
for _ in range(k):
    ans = simulate()

print(ans)