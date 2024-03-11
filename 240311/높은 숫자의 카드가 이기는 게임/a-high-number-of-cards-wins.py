from collections import deque

n = int(input())
b_arr = []
a_arr = []
for _ in range(n):
    b_arr.append(int(input()))


for i in range(1, 2 * n + 1):
    if i in b_arr:
        continue
    else:
        a_arr.append(i)

a_arr.sort()

res = 0

for i in range(n):
    if a_arr and min(a_arr) > b_arr[i]:
        a_arr.pop(0)
        res += 1
    if a_arr and min(a_arr) < b_arr[i] and max(a_arr) < b_arr[i]:
        a_arr.pop(0)
    if a_arr and max(a_arr) > b_arr[i]:
        a_arr.pop()
        res +=1

print(res)