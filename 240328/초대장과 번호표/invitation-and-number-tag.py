n, g = map(int, input().split())

invited = set()
invited.add(1)

for _ in range(g):
    group = list(map(int, input().split()))
    k = group[0]

    count = 0
    not_invited = []

    for i in range(1, len(group)):
        if group[i] in invited:
            count += 1
        else:
            not_invited.append(group[i])

    if count == k - 1:
        for ni in not_invited:
            invited.add(ni)

print(len(invited))