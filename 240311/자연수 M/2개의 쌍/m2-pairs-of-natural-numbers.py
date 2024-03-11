n = int(input())
m = 0
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
    m += x


arr = sorted(arr, key = lambda x: x[1])

# print(arr)

res = -int(1e9)
cur_idx = 0
comp_idx = n - 1

while cur_idx <= comp_idx:
    
    cur_cnt, cur_val = arr[cur_idx]
    comp_cnt, comp_val = arr[comp_idx]

    if cur_cnt == comp_cnt:
        res = max(res, cur_val + comp_val)
        comp_idx -= 1
        cur_idx += 1
    elif cur_cnt < comp_cnt:
        res = max(res, cur_val + comp_val)
        arr[comp_idx] = (comp_cnt - cur_cnt, comp_val)
        cur_idx += 1
    else:
        res = max(res, cur_val + comp_val)
        arr[cur_idx] = (cur_cnt - comp_cnt, cur_val)
        comp_idx -= 1

print(res)