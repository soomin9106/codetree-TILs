n, k = map(int, input().split())

arr = [0] + list(map(int, input().split()))
prefix_sum = [0] * (n + 1)

for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

cnt = 0
for i in range(1, n + 1):
    for j in range(0, n - i + 1):
        res = prefix_sum[j + i] - prefix_sum[j]
        
        if res == k:
            cnt += 1

print(cnt)