n, t = map(int, input().split())
r, c, direction = map(str, input().split())

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

r = int(r) - 1
c = int(c) - 1
d = mapper[direction]

dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


t_cnt = 0


while t_cnt < t:
    cur_r, cur_c = r + dxs[d], c + dys[d]

    if not in_range(cur_r, cur_c):
        d = 3 - d  
    else:
        r,c = cur_r, cur_c
    
    t_cnt += 1

print(r + 1, c + 1)