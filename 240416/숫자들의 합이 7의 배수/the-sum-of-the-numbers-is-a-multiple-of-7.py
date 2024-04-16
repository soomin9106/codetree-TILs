n = int(input())

arr = [0]

for _ in range(n):
    arr.append(int(input()))

prefix_sum = [0] * (n + 1)

# 구간 [i, j] 에서
# prefix_sum[j] - prefix_sum[i - 1] 이 7의 배수가 되어야 함
r = dict()

for i in range(1, n + 1):
    prefix_sum[i] = ((prefix_sum[i - 1] % 7) + arr[i]) % 7

for i in range(1, n + 1):
    if prefix_sum[i] not in r:
        r[prefix_sum[i]] = (i, int(1e9))

    else:
        minimum, _ = r[prefix_sum[i]]
        r[prefix_sum[i]] = (minimum, i)


ans = 0
for key in r:
    mini, maxi = r[key]
    if maxi != int(1e9):
        ans = max(ans, maxi - mini)

print(ans)