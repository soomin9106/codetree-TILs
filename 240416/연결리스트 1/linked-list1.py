class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# cur 앞에 singleton 삽입
def insertPrev(cur, singleton):
    singleton.prev = cur.prev
    singleton.next = cur

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

# cur 뒤에 singleton 삽입
def insertNext(cur, singleton):
    singleton.prev = cur
    singleton.next = cur.next

    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

def print_node(target):
    n = '(Null)'

    if target.prev is None:
        print(n, end = ' ')
    else:
        print(target.prev.data, end = ' ')

    print(target.data, end = ' ')

    if target.next is None:
        print(n)
    else:
        print(target.next.data)

    # print()

s_init = input()
cur = Node(s_init)
n = int(input())

for _ in range(n):
    commands = list(map(str, input().split()))
    opt = int(commands[0])

    if opt == 1:
        val = commands[1]
        singleton = Node(val)

        insertPrev(cur, singleton)

    if opt == 2:
        val = commands[1]
        singleton = Node(val)
        insertNext(cur, singleton)

    if opt == 3:
        if cur.prev:
            cur = cur.prev

    if opt == 4:
        if cur.next:
            cur = cur.next

    print_node(cur)