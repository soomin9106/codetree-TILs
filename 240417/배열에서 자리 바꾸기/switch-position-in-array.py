class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

n = int(input())
q = int(input())

base = [None] + [Node(i) for i in range(1, n + 1)] + [None]
head = base[1]

for i in range(1, n + 1):
    base[i].prev = base[i - 1]
    base[i].next = base[i + 1]


def connect(s, e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

def change(a, b, c, d):
    global head

    if base[c] == head:
        head = base[a]
    elif base[a] == head:
        head = base[c]

    if base[b].next == base[c]:
        connect(base[c].prev, base[d].next)
        connect(base[a].prev, base[c])
        connect(base[d], base[a])
    elif base[d].next == base[a]:
        connect(base[a].prev, base[b].next)
        connect(base[c].prev, base[a])
        connect(base[b], base[c])
    else:
        start = base[c].prev
        end = base[d].next

        connect(base[c].prev, base[d].next)
        connect(base[a].prev, base[c])
        connect(base[d], base[a])

        connect(base[a].prev, base[b].next)
        connect(start, base[a])
        connect(base[b], end)


for _ in range(q):
    a, b, c, d = map(int, input().split())
    change(a,b,c,d)

while head is not None:
    print(head.data, end = ' ')
    head = head.next