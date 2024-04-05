n, q = map(int, input().split())

group1 = [0] * (n + 1)
group2 = [0] * (n + 1)
group3 = [0] * (n + 1)

for i in range(1, n + 1):
    g = int(input())

    if g == 1:
        group1[i] = group1[i - 1] + 1
        group2[i] = group2[i - 1]
        group3[i] = group3[i - 1]

    elif g == 2:
        group1[i] = group1[i - 1] 
        group2[i] = group2[i - 1] + 1
        group3[i] = group3[i - 1]

    else:
        group1[i] = group1[i - 1] 
        group2[i] = group2[i - 1]
        group3[i] = group3[i - 1] + 1

for _ in range(q):
    s, e  = map(int, input().split())

    print(group1[e] - group1[s - 1], group2[e] - group2[s - 1], group3[e] - group3[s - 1])