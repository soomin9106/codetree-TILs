n,k = map(int,input().split())

arr = list(map(int,input().split()))
count = dict()
ans = 0

for a in arr:
    if a in count:
        count[a] += 1
    else:
        count[a] = 1

for i in range(n):
    count[arr[i]] -= 1
    for j in range(i):
        diff = k - arr[i] - arr[j]

        if diff in count:
            ans += count[diff]

print(ans)