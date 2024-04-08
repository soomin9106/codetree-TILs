class Node:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None



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

def pop(u):
    if u.prev is not None:
        u.prev.next = u.next

    if u.next is not None:
        u.next.prev = u.prev
    
    u.prev = u.next = None


n = int(input())
q = int(input())

nodes = [None] + [Node(i) for i in range(1, n+1)]

for _ in range(q):
    inputs = list(map(int, input().split()))

    option = inputs[0]
    i = inputs[1]

    if option == 1:
        pop(nodes[i])
    
    elif option == 2:
        j = inputs[2]
        insertPrev(nodes[i], nodes[j])
    elif option == 3:
        j = inputs[2]
        insertNext(nodes[i], nodes[j])
    elif option == 4:
        print((0 if nodes[i].prev is None else nodes[i].prev.id), (0 if nodes[i].next is None else nodes[i].next.id))

print(' '.join(str(0 if nodes[i].next is None else nodes[i].next.id) for i in range(1, n+1)))