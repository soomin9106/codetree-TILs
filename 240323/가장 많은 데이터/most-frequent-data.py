from collections import defaultdict

n = int(input())
str_dict = defaultdict(int)


for _ in range(n):
    str_dict[input()] += 1

str_dict = sorted(str_dict.items(), key=lambda item: -item[1])

print(str_dict[0][1])