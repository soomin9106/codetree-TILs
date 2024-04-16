class Node:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

def pop(u):
    if u.prev is not None:
        u.prev.next = u.next
    if u.next is not None:
        u.next.prev = u.prev

    u.next = u.prev = None

def insertPrev(u, singleton):
    singleton.prev = u.prev
    singleton.next = u

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

def insertNext(u, singleton):
    singleton.prev = u
    singleton.next = u.next

    if singleton.prev is not None:
        singleton.prev.next = singleton

    if singleton.next is not None:
        singleton.next.prev = singleton


n = int(input())
q = int(input())

nodes = [None] + [Node(i) for i in range(1, n + 1)]

for _ in range(q):
    commands = list(map(int, input().split()))

    opt = commands[0]
    i = commands[1]

    if opt == 1:
        pop(nodes[i])

    elif opt == 2:
        j = commands[2]
        insertPrev(nodes[i], nodes[j])

    elif opt == 3:
        j = commands[2]
        insertNext(nodes[i], nodes[j])

    else:
        if nodes[i].prev is None:
            print(0, end = ' ')
        else:
            print(nodes[i].prev.id, end = ' ')
        

        if nodes[i].next is None:
            print(0)
        else:
            print(nodes[i].next.id)

for i in range(1, n + 1):
    if nodes[i].next:
        print(nodes[i].next.id, end = ' ')
    else:
        print(0, end = ' ')