import heapq

n, m, k = map(int, input().split())

arrn = list(map(int, input().split()))
arrm = list(map(int, input().split()))

arrn.sort()
arrm.sort()

pq = []

for i in range(n):
    heapq.heappush(pq, (arrn[i] + arrm[0], i, 0))

for i in range(k - 1):
    _, idx1, idx2 = heapq.heappop(pq)

    idx2 += 1

    if idx2 < m:
        heapq.heappush(pq, (arrn[idx1] + arrm[idx2], idx1, idx2))

answer, _, _ = heapq.heappop(pq)

print(answer)