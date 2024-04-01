import heapq

n = int(input())

arr = []
for i in range(n):
    a, t = map(int, input().split())
    arr.append((i, a, t))

arr = sorted(arr, key = lambda x: x[1])

pq = []
waiting_time = [0] * n
exit_time = 0

for i in range(n):
    idx, a, t = arr[i][0], arr[i][1], arr[i][2]

    while a > exit_time and pq:
        cur_idx, cur_a, cur_t = heapq.heappop(pq)

        waiting_time[cur_idx] = exit_time - cur_a
        exit_time += cur_t

    if a > exit_time:
        exit_time = a + t
        waiting_time[idx] = 0
    else:
        heapq.heappush(pq, (idx, a, t))

while pq:
    cur_idx, cur_a, cur_t = heapq.heappop(pq)

    waiting_time[cur_idx] = exit_time - cur_a
    exit_time += cur_t


print(max(waiting_time))