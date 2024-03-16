n = int(input())
arr = list(map(int, input().split()))
new_arr = []


for idx, a in enumerate(arr):
    new_arr.append(a)
    new_arr.sort()

    if idx % 2 == 0:
        print(new_arr[len(new_arr) // 2], end = ' ')