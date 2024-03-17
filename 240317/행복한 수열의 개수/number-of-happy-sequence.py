n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))


def is_happy_sequence(ar):
    cnt = 1
    if cnt >= m:
        return True
    for i in range(1, len(ar)):
        if cnt >= m:
            return True
        if ar[i] == ar[i - 1]:
            cnt += 1

            if cnt >= m:
                return True
        else:
            cnt = 1

    return False


res = 0

for i in range(n):
    if is_happy_sequence(arr[i]):
        res += 1

for i in range(n):
    new_arr = []
    for j in range(n):
        new_arr.append(arr[j][i])
    # print(new_arr)
    if is_happy_sequence(new_arr):
        res += 1

print(res)