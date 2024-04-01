import heapq

t = int(input())

for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    pq1 = [] # max_heap
    pq2 = [] # min_heap
    mid = arr[0]

    print(mid, end = ' ')
    for idx, a in enumerate(arr[1:], 1):
        if a > mid:
            heapq.heappush(pq2, a)
        else:
            heapq.heappush(pq1, -a)

        if idx % 2 == 0:
            if len(pq1) < len(pq2):
                heapq.heappush(pq1, -1 * mid)
                mid = heapq.heappop(pq2)

            elif len(pq1) > len(pq2):
                heapq.heappush(pq2, mid)
                mid = -1 * (heapq.heappop(pq1))

            print(mid, end = ' ')
    print()