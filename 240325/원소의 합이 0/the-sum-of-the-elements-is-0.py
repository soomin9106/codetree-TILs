n = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
c_lst = list(map(int, input().split()))
d_lst = list(map(int, input().split()))

ab_dict = dict()

for i in range(n):
    for j in range(n):
        val = a_lst[i] + b_lst[j]
        if val in ab_dict:
            ab_dict[val] += 1
        else:
            ab_dict[val] = 1


ans = 0
for i in range(n):
    for j in range(n):
        cd_sum = c_lst[i] + d_lst[j]

        if (-1 * cd_sum) in ab_dict:
            ans += ab_dict[(-1 * cd_sum)]

print(ans)