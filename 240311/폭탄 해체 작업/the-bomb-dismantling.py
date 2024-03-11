import heapq
n = int(input())

arr = []
for _ in range(n):
    score, limit = map(int, input().split())
    arr.append((limit, score))

arr = sorted(arr, key = lambda x: x[0])



def get_time_limit(idx):
    limit, _ = arr[idx]
    return limit

def get_scroe(idx):
    _, score = arr[idx]
    return score

MAX_T = 10000
bomb_idx = n - 1
pq = []
ans = 0

for i in range(MAX_T, 0, -1):
    while bomb_idx >= 0 and get_time_limit(bomb_idx) >= i:
        heapq.heappush(pq, -get_scroe(bomb_idx))
        bomb_idx -= 1
    
    if pq:
        ans += -heapq.heappop(pq)

print(ans)