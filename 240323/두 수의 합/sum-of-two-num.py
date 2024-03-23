from collections import defaultdict

n, k = map(int, input().split())

arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
arr_cnt = defaultdict(int)

for a in arr:
    arr_cnt[a] += 1

# 3, 4, 5, 6, 7

start = 0
end = n - 1
pairs = []

while start < end:
    temp = arr[start] + arr[end]
    if temp == k:
        pairs.append((arr[start], arr[end]))
        start += 1
        end -= 1
    
    if temp > k:
        end -= 1
    
    if temp < k:
        start += 1

res = 0

for pair in pairs:
    i, j = pair
    res += (arr_cnt[i] * arr_cnt[j])

print(res)