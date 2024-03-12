n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s , e))

arr = sorted(arr, key = lambda x: x[1])

# print(arr)
res = 1
point = arr[0][1]
for i in range(1, len(arr)):
    if arr[i][0] >= point:
        res += 1
        point = arr[i][1]

print(n - res)