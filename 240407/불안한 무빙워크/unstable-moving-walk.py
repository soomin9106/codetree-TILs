n, k = map(int, input().split())

# 안정성 - 사람 유무 체크
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
    # 안정성이 0 이상이고, 사람이 그곳에 없어야 이동 가능
    return s > 0 and not o

def move(idx):
    cur_s, _ = u[idx]
    u[idx] = (cur_s, False)

    if idx + 1 < n:
        n_s, _ = u[idx + 1]
        u[idx + 1] = (n_s - 1, True)


def move_all():
    for i in range(n -1 , -1, -1):
        _, o = u[i]
        if o and can_go(i + 1):
            move(i)

def add():
    s, o = u[0]

    if s > 0 and not o:
        u[0] = (s - 1, True)

def simulate():
    shift()

    move_all()

    add()

    _, o = u[n -1]
    if o:
        move(n - 1)

def done():
    unstable_cnt = 0

    for s, _ in u:
        if not s:
            unstable_cnt += 1

    for s, _ in d:
        if not s:
            unstable_cnt += 1

    return unstable_cnt >= k 

row = list(map(int, input().split()))
for i, s in enumerate(row[:n]):
    u[i] = (s, False)

for i, s in enumerate(row[n:]):
    d[i] = (s, False)

answer = 0

while not done():
    simulate()
    answer += 1

print(answer)