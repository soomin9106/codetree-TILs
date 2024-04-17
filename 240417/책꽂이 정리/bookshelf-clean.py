class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, k = map(int, input().split())
q = int(input())

heads = [0] * (k + 1)
tails = [0] * (k + 1)


def empty(line_num):
    return heads[line_num] == 0

def connect(s, e):
    if s:
        s.next = e
    if e:
        e.prev = s

nodes = [None] + [Node(i) for i in range(1, n + 1)]

for i in range(1, n):
    connect(nodes[i], nodes[i + 1])

heads[1] = 1
tails[1] = n


def pop_front(line_num):
    ret = nodes[heads[line_num]]

    if not ret:
        return None

    if not ret.next:
        heads[line_num] = 0
    else:
        heads[line_num] = ret.next.data

    ret.next = None

    if heads[line_num] != 0:
        nodes[heads[line_num]].prev = None
    else:
        tails[line_num] = 0

    return ret

def pop_back(line_num):
    ret = nodes[tails[line_num]]

    if not ret:
        return None

    if not ret.prev:
        tails[line_num] = 0
    else:
        tails[line_num] = ret.prev.data

    ret.prev = None

    if tails[line_num] != 0:
        nodes[tails[line_num]].next = None
    else:
        heads[line_num] = 0

    return ret

def push_front(line_num, u):
    if heads[line_num] == 0:
        tails[line_num] = heads[line_num] = u.data

    else:
        connect(u, nodes[heads[line_num]])
        heads[line_num] = u.data

def push_back(line_num, u):
    if tails[line_num] == 0:
        tails[line_num] = heads[line_num] = u.data

    else:
        connect(nodes[tails[line_num]], u)
        tails[line_num] = u.data

def move_all_front(i , j):
    if i == j or empty(i):
        return 


    if empty(j):
        heads[j] = heads[i]
        tails[j] = tails[i]

    else:
        connect(nodes[tails[i]], nodes[heads[j]])
        heads[j] = heads[i]

    heads[i] = tails[i] = 0

def move_all_back(i, j):
    if i == j or empty(i):
        return 

    if empty(j):
        heads[j] = heads[i]
        tails[j] = tails[i]

    else:
        connect(nodes[tails[j]], nodes[heads[i]])
        tails[j] = tails[i]

    heads[i] = tails[i] = 0

for _ in range(q):
    opt, i, j = map(int, input().split())

    if opt == 1:
        target = pop_front(i)
        if target:
            push_back(j, target)

    elif opt == 2:
        target = pop_back(i)
        if target:
            push_front(j, target)

    elif opt == 3:
        move_all_front(i, j)
    else:
        move_all_back(i, j)

for i in range(1, k + 1):
    cnt = 0

    cur = nodes[heads[i]]
    while cur != None:
        cnt += 1
        cur = cur.next
    print(cnt, end = "")

    cur = nodes[heads[i]]
    while cur != None:
        print(f" {cur.data}", end ="")
        cur = cur.next

    print()