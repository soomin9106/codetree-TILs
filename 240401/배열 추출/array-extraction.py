import heapq

n = int(input())

pq = []

for _ in range(n):
    val = int(input())
    if val == 0:
        if len(pq) == 0:
            print(0)
        else:
            popped = heapq.heappop(pq)
            print(-1 * popped)

    else:
       heapq.heappush(pq, -val)