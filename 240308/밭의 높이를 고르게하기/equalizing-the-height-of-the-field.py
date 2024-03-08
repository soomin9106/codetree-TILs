import sys

n, t, h = map(int, input().split())
arr = list(map(int, input().split()))

res = int(1e9)

for i in range(0, len(arr) - t + 1):
    temp = arr[i: i + t]
    # print(temp)
    val = 0 
    for item in temp:
        val += abs(item - h)
    
    res = min(res, val)

print(res)