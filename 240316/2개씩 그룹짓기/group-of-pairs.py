n = int(input())
arr = list(map(int, input().split()))

arr.sort()

matches = []
for i in range(n):
    matches.append([arr[i], arr[2*n - i - 1]])

res = -int(1e9)

for mat in matches:
    res = max(res, sum(mat))

print(res)