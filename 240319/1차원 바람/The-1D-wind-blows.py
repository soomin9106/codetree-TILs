n, m, q = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

winds = []

for _ in range(q):
    row, direction = map(str, input().split())
    winds.append((int(row) - 1, direction))

def push(a, direction):
    # print(a)
    if direction == 'L':
        temp = a[m-1]
        for i in range(m-1, 0, -1):
            a[i] = a[i-1]
        a[0] = temp
    else:
        temp = a[0]
        for i in range(1, m):
            a[i - 1] = a[i]
        a[m-1] = temp

    return a

def compare_rows(a, b):
    for i in range(len(a)):
        if a[i] == b[i]:
            return True

    return False

# 시작점으로부터 전파하는 시뮬레이션 1회
def do_simulate(row, direction):
    new_row = push(arr[row], direction)
    arr[row] = new_row

    directions = [''] * n
    directions[row] = direction

    for i in range(row-1, -1, -1):
        if directions[i + 1] == 'L':
            directions[i] = 'R'
        else:
            directions[i] = 'L'

    for i in range(row+1, n):
        if directions[i -1] == 'L':
            directions[i] = 'R'
        else:
            directions[i] = 'L'

    # print(directions)
    # 위에 전파
    for i in range(row-1, -1, -1):
        if compare_rows(arr[i + 1], arr[i]):
            new_a = push(arr[i], directions[i])
            arr[i] = new_a 
        else:
            break
    # 아래에 전파
    for i in range(row+1, n):
        if compare_rows(arr[i -1], arr[i]):
            new_a = push(arr[i], directions[i])
            arr[i] = new_a 
        else:
            break



for item in winds:
    row, direction = item
    do_simulate(row, direction)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()