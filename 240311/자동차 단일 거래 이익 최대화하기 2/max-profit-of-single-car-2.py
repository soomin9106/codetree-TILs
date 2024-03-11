n = int(input())
arr = list(map(int, input().split()))

res = -int(1e9)

for i in range(n):
    for j in range(i + 1, n):
        res = max(res, arr[j] - arr[i])

if res < 0 :
    print(0)
    exit(0)

print(res)