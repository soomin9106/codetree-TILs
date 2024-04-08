r, c, k = map(int, input().split())

MAX_N = 100
MAX_NUM = 100

n, m = 3, 3

grid = [
    [0 for _ in range(2* MAX_N + 1)]
    for _ in range(2 * MAX_N + 1)
]

def row_play(row):
    pairs = list()

    for num in range(1, MAX_NUM + 1):
        frequency = sum([
            1
            for col in range(1, m + 1)
            if grid[row][col] == num
        ])

        if frequency:
            pairs.append((frequency, num))

    for col in range(1, m + 1):
        grid[row][col] = 0

    pairs.sort()

    for i, (frequency, num) in enumerate(pairs):
        grid[row][i * 2 + 1] = num
        grid[row][i * 2 + 2] = frequency

    return len(pairs) * 2


def col_play(col):
    pairs = list()

    for num in range(1, MAX_NUM + 1):
        frequency = sum([
            1 
            for row in range(1, n + 1)
            if grid[row][col] == num
        ])

        if frequency:
            pairs.append((frequency, num))

    for row in range(1, n + 1):
        grid[row][col] = 0

    pairs.sort()

    for i, (frequency, num) in enumerate(pairs):
        grid[i * 2 + 1][col] = num
        grid[i * 2 + 2][col] = frequency

    return len(pairs) * 2
    

def simulate():
    global n, m

    if n >= m:
        m = max([
            row_play(row) for row in range(1, n + 1)
        ])

    else:
        n = max([
            col_play(col) for col in range(1, m + 1)
        ])

for i in range(1, n + 1):
    given_row = list(map(int, input().split()))
    for j, elem in enumerate(given_row, start=1):
        grid[i][j] = elem

ans = -1
for t in range(0, 100):
    if grid[r][c] == k:
        ans = t
        break

    simulate()

print(ans)