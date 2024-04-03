n, k , b = map(int, input().split())

arr = [1 for _ in range(n + 1)]

for _ in range(b):
    val = int(input())
    arr[val] = 0

prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

# print(prefix_sum)


answer = int(1e9)
for i in range(1, n - k + 2):
    val = prefix_sum[i + k - 1] - prefix_sum[i] + arr[i]
    answer = min(answer, k - val)

print(answer)