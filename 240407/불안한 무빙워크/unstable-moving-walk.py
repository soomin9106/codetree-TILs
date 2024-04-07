n, k = map(int, input().split())

u = [(0, False) for _ in range(n)]
d = [(0, False) for _ in range(n)]

def shift():
    temp = u[n - 1]

    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]

    u[0] = d[n - 1]

    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    
    d[0] = temp

def can_go(idx):
    if idx == n:
        return True 

    s, o = u[idx]
    return s > 0 and not o

def move(idx):
    sta, occupied = u[idx]

    u[idx] = (sta, False)

    if idx + 1 < n:
        ns, _ = u[idx + 1]
        u[idx + 1] = (ns - 1, True)

def move_all():
    for i in range(n - 1, -1, -1):
        cur_s, cur_o = u[i]

        if cur_o and can_go(i + 1):
            move(i)

def add():
    s, o = u[0]

    if not o and s > 0:
        u[0] = (s - 1, True)

def done():
    k_cnt = 0
    for item in u:
        s, o = item
        if s == 0:
            k_cnt += 1

    for item in d:
        s, o = item

        if s == 0:
            k_cnt += 1

    return k_cnt >= k

def simulate():
    shift()

    move_all()

    add()

    _, o = u[n - 1]
    if o:
        move(n - 1)

answer = 0
given_row = list(map(int, input().split()))
for i, stability in enumerate(given_row[:n]):
    u[i] = (stability, False)
for i, stability in enumerate(given_row[n:]):
    d[i] = (stability, False)

while not done():
    simulate()
    answer += 1

print(answer)