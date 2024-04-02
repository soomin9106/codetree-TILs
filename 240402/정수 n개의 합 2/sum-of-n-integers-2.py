n, k = map(int, input().split())

arr = list(map(int, input().split()))
prefix_sum = [0] * n

prefix_sum[0] = arr[0]

for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

ranges = []

for i in range(0, len(arr) - k + 1):
    ranges.append((i, i + k - 1))

answer = -int(1e9)
for r in ranges:
    s, e = r
    if s == e:
        answer = max(answer, arr[s])
    else:
        answer = max(answer, prefix_sum[e] - prefix_sum[s] + arr[s])

print(answer)