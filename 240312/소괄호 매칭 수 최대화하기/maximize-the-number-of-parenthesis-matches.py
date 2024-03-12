from functools import cmp_to_key

n = int(input())

arr = []

for _ in range(n):
    s = input()
    arr.append([s.count("("), s.count(")"), s])

def comp(a, b):
    if a[0] * b[1] > a[1] * b[0]:
        return -1
    else:
        return 1
    return 0

arr = sorted(arr, key = cmp_to_key(comp))

new_str = ""
for i in range(len(arr)):
    new_str += arr[i][2]

stack = []
ans = 0
for i in range(len(new_str)):
    if new_str[i] == "(":
        stack.append("(")
    else:
        ans += len(stack)

print(ans)