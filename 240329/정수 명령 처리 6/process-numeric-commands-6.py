import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)

    def size(self):
        return len(self.items)

    def empty(self):
        return not self.items

    def pop(self):
        if self.empty():
            raise Exception("empty queue")
        return -heapq.heappop(self.items)

    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
                        
        return -self.items[0]

pq = PriorityQueue()
n = int(input())

for _ in range(n):
    commands = list(map(str, input().split()))

    if commands[0] == 'push':
        pq.push(int(commands[1]))
    if commands[0] == 'pop':
        print(pq.pop())
    if commands[0] == 'size':
        print(pq.size())
    if commands[0] == 'empty':
        print(1 if pq.empty() else 0)
    if commands == 'top':
        print(pq.top())