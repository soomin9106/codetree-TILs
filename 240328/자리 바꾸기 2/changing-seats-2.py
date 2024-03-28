from collections import defaultdict

n, k = map(int, input().split())

arr = [0]
for i in range(1, n + 1):
    arr.append(i)

seat_dict = defaultdict(set)

for i in range(1, n+1):
    seat_dict[i].add(i)

ks = []
for _ in range(k):
    a, b = map(int, input().split())
    ks.append((a, b))

for i in range(3 * k):
    order = i % k
    a, b = ks[order]

    arr[a], arr[b] = arr[b], arr[a]

    if b not in seat_dict[arr[a]]:
        seat_dict[arr[a]].add(b)

    if a not in seat_dict[arr[b]]:
        seat_dict[arr[b]].add(a)

for sd in seat_dict:
    print(len(seat_dict[sd]))