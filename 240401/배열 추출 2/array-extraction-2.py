import heapq

n = int(input())

pq = []

for _ in range(n):
    val = int(input())

    if val == 0:
        if len(pq) == 0:
            print(0)
        else:
            ans = heapq.heappop(pq)
            print(ans[1])

    else:
        heapq.heappush(pq, (abs(val), val))