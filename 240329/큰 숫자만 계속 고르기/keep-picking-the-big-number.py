import heapq

n, m = map(int, input().split())

arr = list(map(int, input().split()))
for idx, a in enumerate(arr):
    arr[idx] = -a
    

heapq.heapify(arr)

for _ in range(m):
    max_val = heapq.heappop(arr)
    max_val += 1

    heapq.heappush(arr, max_val)

print(abs(arr[0]))