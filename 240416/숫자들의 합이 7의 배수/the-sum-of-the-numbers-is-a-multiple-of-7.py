n = int(input())

arr = [0]

for _ in range(n):
    arr.append(int(input()))

prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = ((prefix_sum[i - 1] % 7) + arr[i]) % 7

# print(prefix_sum)

ans = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if prefix_sum[j] == prefix_sum[i - 1]:
            ans = max(j - i + 1, ans)

print(ans)