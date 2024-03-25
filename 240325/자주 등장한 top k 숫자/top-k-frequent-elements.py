n, k = map(int, input().split())

arr = list(map(int, input().split()))

count = dict()

for a in arr:
    if a in count:
        count[a] += 1
    else:
        count[a] = 1

count_lst = sorted(count.items(), key=lambda item: (-item[1], -item[0]))
# print(count_lst)

for idx in range(k):
    print(count_lst[idx][0], end = ' ')