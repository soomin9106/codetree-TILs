import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []

for a in arr:
    heapq.heappush(pq, -a)

while len(pq) >= 2:
    l1 = heapq.heappop(pq)
    l2 = heapq.heappop(pq)

    l1 *= -1
    l2 *= -1

    if l1 - l2 != 0:
        heapq.heappush(pq, -1 * abs(l1 - l2))

if len(pq) == 1:
    print(-1 * pq[0])
else:
    print(-1)