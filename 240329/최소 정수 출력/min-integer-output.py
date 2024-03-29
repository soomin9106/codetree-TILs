import heapq

n = int(input())

pq = []

for _ in range(n):
    val = int(input())

    if val == 0:
        if len(pq) >= 1:
            print(heapq.heappop(pq))
        else:
            print(0)

    else:
        heapq.heappush(pq, val)