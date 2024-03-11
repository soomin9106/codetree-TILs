import sys
import heapq

n = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)
res = 0

while len(arr) > 1:
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)

    # 비용 계산 및 결과 배열에 추가
    cost = first + second
    res += cost
    heapq.heappush(arr, cost)

print(res)