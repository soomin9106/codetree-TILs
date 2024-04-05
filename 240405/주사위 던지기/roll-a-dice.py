n, m, r, c = map(int, input().split())

actions = list(map(str, input().split()))
arr = [[0] * n for _ in range(n)]

r -= 1
c -= 1

# 초기 
# 위, 뒤, 오, 왼, 앞, 바닥 기준
dir_arr = [1, 5, 3, 4, 2, 6]

arr[r][c] = dir_arr[5]

def turn(dir_arr, direction):
    new_dir_arr = []
    if direction == 'L':
        new_dir_arr.append(dir_arr[2])
        new_dir_arr.append(dir_arr[1])
        new_dir_arr.append(dir_arr[5])
        new_dir_arr.append(dir_arr[0])
        new_dir_arr.append(dir_arr[4])
        new_dir_arr.append(dir_arr[3])

    if direction == 'R':
        new_dir_arr.append(dir_arr[3])
        new_dir_arr.append(dir_arr[1])
        new_dir_arr.append(dir_arr[0])
        new_dir_arr.append(dir_arr[5])
        new_dir_arr.append(dir_arr[4])
        new_dir_arr.append(dir_arr[2])

    if direction == 'U':
        new_dir_arr.append(dir_arr[4])
        new_dir_arr.append(dir_arr[0])
        new_dir_arr.append(dir_arr[2])
        new_dir_arr.append(dir_arr[3])
        new_dir_arr.append(dir_arr[5])
        new_dir_arr.append(dir_arr[1])

    if direction == 'D':
        new_dir_arr.append(dir_arr[1])
        new_dir_arr.append(dir_arr[5])
        new_dir_arr.append(dir_arr[2])
        new_dir_arr.append(dir_arr[3])
        new_dir_arr.append(dir_arr[0])
        new_dir_arr.append(dir_arr[4])

    return new_dir_arr

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(m):
    direction = actions[i]

    if direction == 'L':
        nr, nc = r, c - 1
    elif direction == 'R':
        nr, nc = r, c + 1
    elif direction == 'U':
        nr, nc = r - 1, c
    else:
        nr, nc = r + 1, c

    if in_range(nr, nc):
        dir_arr = turn(dir_arr, direction)
        arr[nr][nc] = dir_arr[-1]
        r, c = nr, nc
    else:
        break


answer = 0
for a in arr:
    answer += sum(a)

print(answer)