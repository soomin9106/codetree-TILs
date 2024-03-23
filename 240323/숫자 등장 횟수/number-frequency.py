n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr_dict = dict()

for a in arr:
    if a in arr_dict:
        arr_dict[a] += 1
    else:
        arr_dict[a] = 1

m_lst = list(map(int, input().split()))

for item in m_lst:
    if item not in arr_dict:
        print(0, end = ' ')
    else:
        print(arr_dict[item], end = ' ')