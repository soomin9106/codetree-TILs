n, t = map(int, input().split())

arr = []
for _ in range(2):
    arr.append(list(map(int, input().split())))

# 시계 방향 회전 
def do_simulate():
    temp = arr[0][n-1]

    for i in range(n - 2, -1, -1):
        arr[0][i + 1] = arr[0][i]
    
    arr[0][0] = arr[1][n-1]

    # 뒤로 한칸씩 밀기
    for i in range(n - 2, -1, -1):
        arr[1][i + 1] = arr[1][i]
        

    arr[1][0] = temp


for _ in range(t):
    do_simulate()

for i in range(2):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()