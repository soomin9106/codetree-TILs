class Node:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

nodes = {}
nodeId = {}

def connect(s, e):
    if s:
        s.next = e
    if e:
        e.prev = s        

def pop(u):
    connect(u.prev, u.next)
    u.prev = u.next = None

n, m = map(int, input().split())
line = list(map(int, input().split()))

kinghtNum = line[0]
nodeId[kinghtNum] = 1
nodes[1] = Node(kinghtNum)
for i in range(2, n + 1):
    kinghtNum = line[i - 1]
    nodeId[kinghtNum] = i
    nodes[i] = Node(kinghtNum)
    connect(nodes[i - 1], nodes[i])

    if i == n:
        connect(nodes[n], nodes[1])

for _ in range(m):
    kinghtNum = int(input())
    print(nodes[nodeId[kinghtNum]].next.id, nodes[nodeId[kinghtNum]].prev.id)

    pop(nodes[nodeId[kinghtNum]])