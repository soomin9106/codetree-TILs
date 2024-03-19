n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def is_plus_rect(w, h, x, y):
    count = 0

    for i in range(w):
        for j in range(h):
            temp_x, temp_y = x + i, y + j

            if in_range(temp_x, temp_y) and arr[temp_x][temp_y] > 0:
                count += 1
            else:
                return -1

    return count


res = -1
for w in range(1, n+1):
    for h in range(1, m+1):
        for x in range(n):
            for y in range(m):
                res = max(res, is_plus_rect(w, h, x, y))

print(res)