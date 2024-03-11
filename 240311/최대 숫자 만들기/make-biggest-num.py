from functools import cmp_to_key

# 앞자리수 맞춰서 내림차순 정렬
def compare(x, y): 
    if int(x[0]) > int(y[0]):
        return -1
    elif int(x[0]) < int(y[0]):
        return 1
    else:
        if int(x + y) > int(y + x):
            return -1
        elif int(x + y) < int(y + x):
            return 1
        else:
            return 0
    return 0
            



n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

arr = sorted(arr, key = cmp_to_key(compare))

res = ''

for a in arr:
    res += a

print(int(res))