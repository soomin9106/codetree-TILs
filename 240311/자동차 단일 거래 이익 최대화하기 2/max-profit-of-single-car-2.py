n = int(input())
arr = list(map(int, input().split()))

res = -int(1e9)


min_price = arr[0]
for i in range(n):
    res = max(res, arr[i] - min_price)

    if min_price > arr[i]:
        min_price = arr[i]

if res < 0 :
    print(0)
    exit(0)

print(res)