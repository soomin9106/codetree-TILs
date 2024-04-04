n, m, k = map(int, input().split())

arr = []
arr.append([0] * (m + 1))
for _ in range(n):
    s = input()
    temp = [0]
    for item in s:
        temp.append(item)
    
    arr.append(temp)

prefix_a = [[0] * (m + 1) for _ in range(n + 1)]
prefix_b = [[0] * (m + 1) for _ in range(n + 1)]
prefix_c = [[0] * (m + 1) for _ in range(n + 1)]

def calc_prefix_sum(i, j, prefix):
    return prefix[i - 1][j] + \
            prefix[i][j - 1] - \
            prefix[i-1][j-1] + 1

def calc_prefix_sum_none(i, j, prefix):
    return prefix[i - 1][j] + \
            prefix[i][j - 1] - \
            prefix[i-1][j-1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i][j] == 'a':
            prefix_a[i][j] = calc_prefix_sum(i, j, prefix_a)
            prefix_b[i][j] = calc_prefix_sum_none(i, j, prefix_b)
            prefix_c[i][j] = calc_prefix_sum_none(i, j, prefix_c)
        elif arr[i][j]== 'b':
            prefix_b[i][j] = calc_prefix_sum(i, j , prefix_b)
            prefix_a[i][j] = calc_prefix_sum_none(i, j, prefix_a)
            prefix_c[i][j] = calc_prefix_sum_none(i, j, prefix_c)
        else:
            prefix_c[i][j] = calc_prefix_sum(i, j , prefix_c)
            prefix_b[i][j] = calc_prefix_sum_none(i, j, prefix_b)
            prefix_a[i][j] = calc_prefix_sum_none(i, j, prefix_a)

def get_sum_from_each(s1, e1, s2, e2, prefix):
    return prefix[s2][e2] - \
            prefix[s1 - 1][e2] - \
            prefix[s2][e1 - 1] + \
            prefix[s1 - 1][e1 - 1]
            

def get_sum(s1, e1, s2, e2):
    return get_sum_from_each(s1, e1, s2, e2, prefix_a), get_sum_from_each(s1, e1, s2, e2, prefix_b), get_sum_from_each(s1, e1, s2, e2, prefix_c)


for _ in range(k):
    s1, e1, s2, e2 = map(int, input().split())

    aval, bval, cval = get_sum(s1, e1, s2, e2)
    print(aval, bval, cval)