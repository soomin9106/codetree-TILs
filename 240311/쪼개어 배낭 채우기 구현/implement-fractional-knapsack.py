import sys

n, m = map(int, input().split())

arr = []
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((v / w, w, v))

arr = sorted(arr, key = lambda x: -x[0])

# print(arr)
res = 0 
for a in arr:
    weighted_v, w, v = a
    if m - w >= 0:
        m -= w
        res += v
    else:
        cur_val = v * (m / w)
        res += cur_val
        break

formatted_number = f"{res:.3f}"
print(formatted_number)