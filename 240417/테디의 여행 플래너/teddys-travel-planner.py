class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n, q = map(int, input().split())
pinned = None

nodes = [None]

def connect(s, e):
    if s:
        s.next = e
    if e:
        e.prev = s

cities = list(map(str, input().split()))
for city in cities:
    nodes.append(Node(city))

for i in range(1, n):
    connect(nodes[i], nodes[i + 1])

nodes[1].prev = nodes[n]
nodes[n].next = nodes[1]

pinned = nodes[1]

def change_pin_right():
    global pinned
    if pinned.next is None:
        return 

    pinned = pinned.next

def change_pin_left():
    global pinned
    if pinned.prev is None:
        return 

    pinned = pinned.prev

def pop(u):
    if u.prev is not None:
        u.prev.next = u.next
    if u.next is not None:
        u.next.prev = u.prev

    u.next = u.prev = None

def insertNext(u, singleton):
    singleton.prev = u
    singleton.next = u.next

    if singleton.prev is not None:
        singleton.prev.next = singleton

    if singleton.next is not None:
        singleton.next.prev = singleton

for _ in range(q):
    commands = list(map(str, input().split()))
    opt = int(commands[0])

    if opt == 1:
        change_pin_right()
    elif opt == 2:
        change_pin_left()
    elif opt == 3:
        if pinned.next:
            pop(pinned.next)
    else:
        newNode = Node(commands[1])
        insertNext(pinned, newNode)

    if pinned.next is None or pinned.prev is None or pinned.prev.data == pinned.next.data:
        print(-1)
    else:
        print(pinned.prev.data, pinned.next.data)