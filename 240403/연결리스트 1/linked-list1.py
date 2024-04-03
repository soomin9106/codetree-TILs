class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 두 노드를 연결해줌 
def connect(s, e):
    if s:
        s.next = e
    if e:
        e.prev = s

# target 뒤에 s를 삽입
def insertNext(target, s):
    connect(s, target.next)
    connect(target, s)

#  target 앞에 s를 삽입
def insertPrev(target, s):
    connect(target.prev, s)
    connect(s, target)

# target의 이전 노드, target, target의 다음 노드의 값을 출력합니다.
def printNode(target):
    n = "(Null)"

    if target.prev is None:
        print(n, end = ' ')
    else:
        print(target.prev.data, end = ' ')
    print(target.data, end = ' ')

    if target.next is None:
        print(n)
    else:
        print(target.next.data)

s_init = input()
cur = Node(s_init)
n = int(input())

for _ in range(n):
    arr = input().split()
    option = int(arr[0])

    if option == 1:
        data = arr[1]
        target = Node(data)

        insertPrev(cur, target)

    if option == 2:
        data = arr[1]
        target = Node(data)

        insertNext(cur, target)

    if option == 3:
        if cur.prev:
            cur = cur.prev
    
    if option == 4:
        if cur.next:
            cur = cur.next
    
    printNode(cur)