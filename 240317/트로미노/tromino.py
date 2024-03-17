n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

res = -int(1e9)

# 2 * 2 배열 들어오는 경우
def calc_case1(arr):
    
    c1 = arr[0][0] + arr[1][0] + arr[1][1]
    c2 = arr[0][1] + arr[1][0] + arr[1][1]
    c3 = arr[1][0] + arr[0][0] + arr[0][1]
    c4 = arr[1][1] + arr[0][0] + arr[0][1]

    return max(c1, c2, c3, c4)

# 3 * 3 배열 들어오는 경우
def calc_case2(arr):
    c1 = sum(arr[0])
    c2 = sum(arr[1])
    c3 = sum(arr[2])
    c4 = arr[0][0] + arr[1][0] + arr[2][0]
    c5 = arr[0][1] + arr[1][1] + arr[2][1]
    c6 = arr[0][2] + arr[1][2] + arr[2][2]

    return max(c1, c2, c3, c4, c5, c6)

# 2 * 2 배열부터 만들어가면서 체크
for i in range(0, n - 1):
    for j in range(0, m - 1):
        new_arr = []
        for k in range(i, i+2):
            temp = []
            for l in range(j, j+2):
                temp.append(arr[k][l])
            new_arr.append(temp)
        
        res = max(res, calc_case1(new_arr))

# 3 * 3 배열 만들어가면서 체크 
for i in range(0, n - 2):
    for j in range(0, m - 2):
        new_arr = []
        for k in range(i, i+3):
            temp = []
            for l in range(j, j+3):
                temp.append(arr[k][l])
            new_arr.append(temp)
        
        res = max(res, calc_case2(new_arr))

print(res)