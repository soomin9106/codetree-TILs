import heapq

n = int(input())

orders = []
max_time = 0
for _ in range(n):
    p, d = map(int, input().split())
    max_time = max(max_time, d)
    orders.append((d, p))

orders.sort(key = lambda x: x[0])

# print(orders)

answer = 0
curr_time = max_time
pq = []

for order in orders:
    cur_d, cur_p = order
    heapq.heappush(pq, (cur_p, cur_d))

    if len(pq) > cur_d:
        # print(pq)
        heapq.heappop(pq)

for item in pq:
    answer += item[0]

print(answer)