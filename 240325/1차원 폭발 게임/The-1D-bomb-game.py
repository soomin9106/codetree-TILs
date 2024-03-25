n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

def remove_nearby():
    count = 1
    near_idxs = [0]
    nears = []

    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            count += 1
            near_idxs.append(i)
        else:
            if count >= m:
                nears.append(near_idxs)
            count = 1
            near_idxs = [i]

    if len(near_idxs) >= m:
        nears.append(near_idxs)

    for near in nears:
        # print(near[-1], arr)
        s, e = near[0], near[-1]
        if len(arr) >= 1:
            for j in range(s, e+1):
                arr[j] = 0

    temp_arr = []
    is_changed = False

    for i in range(len(arr)):
        if arr[i] != 0:
            temp_arr.append(arr[i])
        else:
            is_changed = True

    return is_changed, temp_arr

while True:
    is_changed, temp_arr = remove_nearby()
    # print(temp_arr)
    if not is_changed:
        print(len(temp_arr))
        for t in temp_arr:
            print(t)
        break
    else:
        arr = temp_arr