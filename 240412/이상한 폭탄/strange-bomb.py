n, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

R = [0] * n
num_dict = dict()


for i in range(n - 1, -1, -1):
    val = arr[i]

    if val not in num_dict:
        R[i] -= 1
    else:
        R[i] = num_dict[val]

    num_dict[val] = i


ans = -1
for i in range(n):
    if R[i] != -1 and abs(R[i] - i) <= k:
        ans = max(ans, arr[i])

print(ans)