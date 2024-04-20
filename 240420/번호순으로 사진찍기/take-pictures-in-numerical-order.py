n, k = map(int, input().split())

hates = []

for _ in range(k):
    x1, x2 = map(int, input().split())
    if x1 > x2:
        hates.append((x2, x1))
    else:
        hates.append((x1, x2))

hates.sort(key=lambda x: x[1])

item = 0
answer = 1
for hate in hates:
    if hate[0] >= item:
        answer += 1
        item = hate[1]

print(answer)