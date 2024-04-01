import heapq

n, m, k = map(int, input().split())

arrn = list(map(int, input().split()))
arrm = list(map(int, input().split()))

arrn.sort()
arrm.sort()

pq = []

for item in arrn:
    heapq.heappush(pq, (item + arrm[0], item, arrm[0]))

cnt = 1
n_idx = 0
m_idx = 1
res = 0


while cnt != k:
    # print(n_idx, m_idx)
    res = heapq.heappop(pq)
    cnt += 1

    heapq.heappush(pq, (arrn[n_idx] + arrm[m_idx], arrn[n_idx], arrm[m_idx]))

    n_idx = (n_idx + 1) % len(arrn)
    if n_idx == 0:
        m_idx += 1


res = heapq.heappop(pq)
print(res[0])