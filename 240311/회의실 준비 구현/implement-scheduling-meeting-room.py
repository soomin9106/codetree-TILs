n = int(input())

arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr = sorted(arr, key = lambda x: x[1])

res = [arr[0]]

for i in range(1, len(arr)):
    cur_s, cur_e = arr[i]
    prev_s, prev_e = res[-1]

    if prev_e <= cur_s:
        res.append(arr[i])

print(len(res))