a = input()

n = len(a)

R = [0] * n

for i in range(n -2, -1, -1):
    if a[i] == ")" and a[i + 1] == ")":
        R[i] = R[i + 1] + 1
    else:
        R[i] = R[i + 1]

ans = 0
for i in range(0, n - 2, 1):
    if a[i] == "(" and a[i + 1] == "(":
        ans += R[i + 2]

print(ans)