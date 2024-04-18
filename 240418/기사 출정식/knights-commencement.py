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

n, m = map(int, input().split())

arr = list(map(int, input().split()))
nodes = [None]

for a in arr:
    nodes.append(Node(a))

for i in range(1, n):
    connect(nodes[i], nodes[i + 1])

nodes[1].prev = nodes[n]
nodes[n].next = nodes[1]

def call(u):
    cur = nodes[1]
    while cur and cur.id != u:
        cur = cur.next
    
    if cur.next is not None:
        print(cur.next.id, end = ' ')
    if cur.prev is not None:
        print(cur.prev.id)

def pop(u):
    cur = nodes[1]
    while cur and cur.id != u:
        cur = cur.next

    if cur.prev is not None:
        cur.prev.next = cur.next
    if cur.next is not None:
        cur.next.prev = cur.prev

    cur.next = cur.prev = None


for _ in range(m):
    cur = int(input())
    # print(cur)
    call(cur)
    pop(cur)