import heapq

n = int(input())
arr = list(map(int, input().split()))

answer = -int(1e9)

pq = []
heapq.heappush(pq, arr[-1])
avg = arr[-1]

for i in range(n - 2, 0, -1):
    pq_len = len(pq)
    heapq.heappush(pq, arr[i])

    if pq[0] == arr[i]:
        continue

    avg = sum(pq[1:]) / (len(pq) - 1)
    if avg > answer:
        # print(pq)
        answer = avg

formatted_number = f"{answer:.2f}"
print(formatted_number)