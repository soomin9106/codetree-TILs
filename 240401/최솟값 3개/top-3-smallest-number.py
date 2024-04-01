import heapq

n = int(input())
arr = list(map(int, input().split()))

pq = []

for a in arr:
    heapq.heappush(pq, a)
    if len(pq) < 3:
        print(-1)
    else:
        i1 = heapq.heappop(pq)
        i2 = heapq.heappop(pq)
        i3 = heapq.heappop(pq)

        print(i1 * i2 * i3)

        heapq.heappush(pq, i1)
        heapq.heappush(pq, i2)
        heapq.heappush(pq, i3)