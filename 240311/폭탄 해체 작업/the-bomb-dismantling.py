n = int(input())

arr = []
for _ in range(n):
    score, limit = map(int, input().split())
    arr.append((limit, score))

arr = sorted(arr, key = lambda x: (x[0], -x[1]))

cur_val = arr[0]
res = cur_val[1]

for i in range(1, len(arr)):
    if arr[i][0] == cur_val[0]:
        continue
    else:
        res += arr[i][1]
        cur_val = arr[i]

print(res)