n = int(input())

times = []
prices = []
for _ in range(n):
    t, p = map(int, input().split())
    times.append(t)
    prices.append(p)
times.append(0)
prices.append(0)

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if times[i] + i <= n:
        dp[i] = max(prices[i] + dp[times[i] + i], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])