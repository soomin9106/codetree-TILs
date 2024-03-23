n, m = map(int, input().split())
str_dict = dict()
num_dict = dict()


for i in range(1, n + 1):
    val = input()
    str_dict[val] = i
    num_dict[i] = val

for _ in range(m):
    val = input()

    if val.isdigit():
        print(num_dict[int(val)])
    else:
        print(str_dict[val])