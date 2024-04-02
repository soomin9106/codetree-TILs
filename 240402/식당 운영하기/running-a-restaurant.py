import heapq

n = int(input())

orders = []
for _ in range(n):
    p, d = map(int, input().split())
    orders.append((p, d))

orders.sort(key = lambda x: (x[1], -x[0]))

pq = []

for order in orders:
    cur_p, cur_d = order
    if pq and abs(pq[0][0]) == cur_d:
        continue
    else:
        heapq.heappush(pq, (-cur_d, cur_p))

answer = 0

for item in pq:
    answer += item[1]

print(answer)