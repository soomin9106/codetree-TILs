n = int(input())

arr = []
for _ in range(n):
    arr.append(input())


arr.sort()

for a in arr:
    print(a)