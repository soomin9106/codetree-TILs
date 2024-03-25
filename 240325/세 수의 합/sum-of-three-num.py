from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(int)
ans = 0

for a in arr:
    count[a] += 1

for i in range(n):
    for j in range(0, i):
        diff = k - arr[i] - arr[j]

        count[arr[i]] -= 1
        # count[arr[j]] -= 1

        if count[diff] > 0:
            ans += 1
        
print(ans)