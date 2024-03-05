import sys
n, s = map(int, input().split())
arr = list(map(int, input().split()))


res = int(1e9)
for i in range(n):
    for j in range(i +1, n):
        new_arr = arr[0: i] + arr[i + 1: j] + arr[j + 1: n]
        # print(new_arr)
        res = min(res, abs(sum(new_arr) - s))

print(res)