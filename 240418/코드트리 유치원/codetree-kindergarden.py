class Node:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

def connect(s, e):
    if s:
        s.next = e
    if e:
        e.prev = s

nodes = {}
nodes[1] = Node(1)
cur_node = 1

def insertNext(u, b):
    global cur_node

    for i in range(1, b + 1):
        nodes[cur_node + i] = Node(cur_node + i)

    for i in range(1, b):
        connect(nodes[cur_node + i], nodes[cur_node + i + 1])

    if u.next is not None:
        connect(nodes[cur_node + b], u.next)
    
    connect(u, nodes[cur_node + 1])

    cur_node += b

def insertPrev(u, b):
    global cur_node

    for i in range(1, b + 1):
        nodes[cur_node + i] = Node(cur_node + i)

    for i in range(1, b):
        connect(nodes[cur_node + i], nodes[cur_node + i + 1])

    if u.prev is not None:
        connect(u.prev, nodes[cur_node + 1])

    connect(nodes[cur_node + b], u)

    cur_node += b

q = int(input())
for _ in range(q):
    commands = list(map(int, input().split()))
    opt = commands[0]

    if opt == 1:
        a, b = commands[1], commands[2]

        insertNext(nodes[a], b)

    elif opt == 2:
        a, b = commands[1], commands[2]

        insertPrev(nodes[a], b)

    else:
        a = commands[1]

        if nodes[a].prev and nodes[a].next:
            print(nodes[a].prev.id, nodes[a].next.id)
        else:
            print(-1)