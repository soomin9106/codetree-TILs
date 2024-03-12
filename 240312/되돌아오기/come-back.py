n = int(input())

arr = []

# N, S, E, W
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

mapper = {
    'N': 0,
    'S': 1,
    'E': 2,
    'W': 3
}


for _ in range(n):
    direction, count = map(str, input().split())
    arr.append((mapper[direction], int(count)))

x, y = 0, 0
sec = 0
flag = 1
for item in arr:
    for _ in range(item[1]):
        x, y = x + dxs[item[0]], y + dys[item[0]]
        # print(x, y)
        sec += 1
        if x == 0 and y == 0:
            flag = 0
            break
    if flag == 0:
        break

if x != 0 or y != 0:
    print(-1)
    exit(0)
print(sec)