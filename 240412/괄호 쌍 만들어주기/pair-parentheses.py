a = input()

open_sets = []
close_sets = []
n = len(a)

for i in range(len(a)):
    if a[i] == "(":
        open_sets.append(i)

opens = []

for i in range(len(open_sets) - 1):
    if abs(open_sets[i] - open_sets[i + 1]) == 1:
        opens.append((open_sets[i], open_sets[i + 1]))

for i in range(len(a)):
    if a[i] == ")":
        close_sets.append(i)

closes = []

for i in range(len(close_sets) - 1):
    if abs(close_sets[i] - close_sets[i + 1]) == 1:
        closes.append((close_sets[i], close_sets[i + 1]))

# print(opens, closes)
ans = 0
for (x , y) in opens:
    for (cx, cy) in closes:
        if y < cx:
            ans += 1

print(ans)